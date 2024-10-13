import os
import numpy as np
from PIL import Image
import pandas as pd
import time


# 通道矩阵求均值，去中心化
def process_channel(channel):
    matrix_mean = np.mean(channel, axis=1, keepdims=True)
    matrix_centered = channel - matrix_mean
    return matrix_centered, matrix_mean


# 实现PCA降维，保留特征向量数自行设置
def PCA_compute(channel_data, explained_variance_ratio):
    U, S, Vt = np.linalg.svd(channel_data, full_matrices=False)
    eigenvalues = S ** 2 / (len(S) - 1)
    ratio = np.cumsum(eigenvalues) / np.sum(eigenvalues)
    n_feature = np.argmax(ratio >= explained_variance_ratio) + 1
    U_reduced = U[:, :n_feature]
    S_reduced = np.diag(S[:n_feature])
    Vt_reduced = Vt[:n_feature, :]
    pca_data = np.dot(U_reduced, S_reduced)
    return pca_data, Vt_reduced, n_feature


# 计算MSE
def calculate_mse(original, reconstructed):
    return np.mean((original - reconstructed) ** 2)


# 计算PSNR
def calculate_psnr(original, reconstructed):
    mse = calculate_mse(original, reconstructed)
    if mse == 0:
        return 100
    max_pixel = 255.0
    return 20 * np.log10(max_pixel / np.sqrt(mse))


# 加载图像并应用PCA，并保存重构后的图像
def apply_and_save_PCA_images(input_folder, output_folder, explained_variance_ratio):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    results = []
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.endswith('.tif'):
                input_path = os.path.join(root, file)
                output_path = os.path.join(output_folder, file)
                image = np.array(Image.open(input_path))

                height, width, channel = image.shape
                reconstructed_image = np.zeros_like(image, dtype=np.float64)

                start_time = time.time()

                for c in range(channel):
                    channel_data = image[:, :, c]
                    channel_centered, channel_mean = process_channel(channel_data)
                    pca_channel_data, eigenvector_subset, n_feature = PCA_compute(channel_centered,
                                                                                  explained_variance_ratio)
                    reconstructed_channel = np.dot(pca_channel_data, eigenvector_subset) + channel_mean
                    reconstructed_image[:, :, c] = reconstructed_channel

                end_time = time.time()
                reconstructed_image = np.clip(reconstructed_image, 0, 255).astype(np.uint8)
                Image.fromarray(reconstructed_image).save(output_path)

                mse = calculate_mse(image, reconstructed_image)
                psnr = calculate_psnr(image, reconstructed_image)
                original_size = os.path.getsize(input_path)
                compressed_size = os.path.getsize(output_path)
                compression_ratio = compressed_size / original_size
                space_saving = (original_size - compressed_size) / original_size
                run_time = end_time - start_time

                results.append({
                    'Image': file,
                    'MSE': mse,
                    'PSNR': psnr,
                    'Original Size': original_size,
                    'Compressed Size': compressed_size,
                    'Compression Ratio': compression_ratio,
                    'Space Saving': space_saving,
                    'Run Time': run_time
                })

    results_df = pd.DataFrame(results)
    results_df.to_csv(os.path.join(output_folder, 'pca_evaluation_results.csv'), index=False)
    return results_df


if __name__ == '__main__':
    input_base_folder = 'E:/pythonProject/DaAlhw2/Images'
    output_base_folder = 'E:/pythonProject/DaAlhw2'
    categories = ['agricultural', 'airplane', 'beach']

    explained_variance_ratios=[0.05,0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    for category in categories:
        for ratio in explained_variance_ratios:
            input_folder = os.path.join(input_base_folder, category)
            output_folder = os.path.join(output_base_folder, f'Images_rev_{ratio}', category)
            apply_and_save_PCA_images(input_folder, output_folder, ratio)
            print(f"finish{ratio}")

