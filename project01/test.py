import sys
import time
import numpy as np
import random
import csv
from collections import defaultdict


class CountMinSketch:
    def __init__(self, initial_width, depth, fill_ratio_threshold=0.8):
        self.width = initial_width
        self.depth = depth
        self.counters = np.zeros((depth, initial_width), dtype=int)
        self.fill_ratio_threshold = fill_ratio_threshold

    def increment(self, key):
        updata_start = time.time()
        if self.fill_ratio() > self.fill_ratio_threshold:
            self.expand()
        for i in range(self.depth):
            hash_val = hash(str(i) + key) % self.width
            self.counters[i, hash_val] += 1
        updata_end = time.time()
        return updata_end - updata_start

    def estimate(self, key):
        min_count = float('inf')
        for i in range(self.depth):
            hash_val = hash(str(i) + key) % self.width
            min_count = min(min_count, self.counters[i, hash_val])
        return min_count

    def fill_ratio(self):
        return np.count_nonzero(self.counters) / (self.width * self.depth)

    def expand(self):
        new_width = self.width * 2
        new_counters = np.zeros((self.depth, new_width), dtype=int)
        for i in range(self.depth):
            for j in range(self.width):
                new_counters[i, j] = self.counters[i, j]
        self.width = new_width
        self.counters = new_counters


class MisraGries:
    def __init__(self, initial_k):
        self.initial_k = initial_k
        self.k = 50 * self.initial_k
        self.items = {}

    def process_item(self, item):
        updata_start = time.time()
        if item in self.items:
            self.items[item] += 1
        elif len(self.items) < self.k - 1:
            self.items[item] = 1
        else:
            for key in list(self.items.keys()):
                self.items[key] -= 1
                if self.items[key] == 0:
                    del self.items[key]
            self.items[item] = self._calculate_frequency()
        updata_end = time.time()
        return updata_end - updata_start

    def _calculate_frequency(self):
        if len(self.items) < self.k // 2:
            return max(1, self.initial_k // 10)
        elif len(self.items) < self.k:
            return max(1, self.initial_k // 5)
        else:
            return max(1, self.initial_k // 2)

    def get_top_k(self):
        return sorted(self.items.items(), key=lambda x: x[1], reverse=True)[:self.initial_k]


def member_query(movieId, timestamp, initial_width, depth, fill_ratio_threshold=0.8):
    update_time = 0.0
    incre_count = 0

    construction_start = time.time()
    count_min_sketch = CountMinSketch(initial_width, depth, fill_ratio_threshold)
    with open('ratings.csv', 'r') as file:
        next(file)
        for line in file:
            _, movie, _, timesta = line.strip().split(',')
            if int(timesta) <= timestamp:
                update_time += count_min_sketch.increment(movie)
                incre_count += 1
    construction_end = time.time()

    query_start = time.time()
    flag = False
    if count_min_sketch.estimate(movieId) > 0:
        flag = True
    query_end = time.time()

    space_occupancy = sys.getsizeof(count_min_sketch.counters.nbytes) + sys.getsizeof(
        count_min_sketch.width) + sys.getsizeof(count_min_sketch.depth) + sys.getsizeof(
        count_min_sketch.fill_ratio_threshold)
    return flag, construction_end - construction_start, update_time / incre_count, query_end - query_start, space_occupancy


def dic_member_query(movieId, timestamp):
    data_dict = {}
    with open('ratings.csv', 'r') as file:
        next(file)
        for line in file:
            _, movie, _, timesta = line.strip().split(',')
            if int(timesta) <= timestamp:
                data_dict[movie] = data_dict.get(movie, 0) + 1
    return movieId in data_dict


def frequency_query(movieId, timestamp, initial_width, depth, fill_ratio_threshold=0.8):
    update_time = 0.0
    incre_count = 0

    construction_start = time.time()
    count_min_sketch = CountMinSketch(initial_width, depth, fill_ratio_threshold)
    with open('ratings.csv', 'r') as file:
        next(file)
        for line in file:
            _, movie, _, timesta = line.strip().split(',')
            if int(timesta) <= timestamp:
                update_time += count_min_sketch.increment(movie)
                incre_count += 1
    construction_end = time.time()

    query_start = time.time()
    freq = count_min_sketch.estimate(movieId)
    if freq == 'inf':
        freq = 0
    query_end = time.time()

    space_occupancy = sys.getsizeof(count_min_sketch.counters.nbytes) + sys.getsizeof(
        count_min_sketch.width) + sys.getsizeof(count_min_sketch.depth) + sys.getsizeof(
        count_min_sketch.fill_ratio_threshold)
    return freq, construction_end - construction_start, update_time / incre_count, query_end - query_start, space_occupancy


def dic_frequency_query(movieId, timestamp):
    data_dict = {}
    with open('ratings.csv', 'r') as file:
        next(file)
        for line in file:
            _, movie, _, timesta = line.strip().split(',')
            if int(timesta) <= timestamp:
                data_dict[movie] = data_dict.get(movie, 0) + 1
    return data_dict.get(movieId, 0)


def top_k_query(k, timestamp):
    update_time = 0.0
    incre_count = 0

    construction_start = time.time()
    misra_gries = MisraGries(k)
    with open('ratings.csv', 'r') as file:
        next(file)
        for line in file:
            _, movie, _, timesta = line.strip().split(',')
            if int(timesta) <= timestamp:
                update_time += misra_gries.process_item(movie)
                incre_count += 1
    construction_end = time.time()

    query_start = time.time()
    top_k_items = misra_gries.get_top_k()
    query_end = time.time()

    space_occupancy = sys.getsizeof(misra_gries.k) + sys.getsizeof(misra_gries.initial_k) + sys.getsizeof(
        misra_gries.items)
    return top_k_items, construction_end - construction_start, update_time / incre_count, query_end - query_start, space_occupancy


def dic_top_k_query(k, timestamp):
    data_dict = {}
    with open('ratings.csv', 'r') as file:
        next(file)
        for line in file:
            _, movie, _, timesta = line.strip().split(',')
            if int(timesta) <= timestamp:
                data_dict[movie] += data_dict.get(movie, 0) + 1

    return sorted(data_dict.items(), key=lambda x: x[1], reverse=True)[:k]


def generate_random_data(file_path, num_queries):
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['movieId', 'timestamp']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(num_queries):
            movieId = random.randint(0, 300000)
            timestamp = random.randint(8000000000, 20000000000)
            writer.writerow({'movieId': movieId, 'timestamp': timestamp})

#
# #生成测试用的100条数据文件
# if __name__ == "__main__":
#     num_queries = 100
#     file_path = 'query.csv'
#     generate_random_data(file_path, num_queries)
#     print(f"{num_queries} pairs of (movieID, timestamp) have been generated and saved to '{file_path}'.")

#member
if __name__ == "__main__":
    with open('query.csv', 'r') as file:
        next(file)
        with open('member_test.csv', 'w', newline='') as csvfile:
            fieldnames = ['result', 'construction_time', 'update_time', 'query_time', 'space_occupancy', 'true_result']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for line in file:
                movieId, timestamp = line.strip().split(',')
                result = member_query(movieId, int(timestamp), initial_width=10000, depth=10)
                true_result = dic_member_query(int(movieId), int(timestamp))
                writer.writerow({
                    'result': result[0],
                    'construction_time': result[1],
                    'update_time': result[2],
                    'query_time': result[3],
                    'space_occupancy': result[4],
                    'true_result': true_result
                })
#
##frequency
# if __name__ == "__main__":
#     with open('query.csv', 'r') as file:
#         next(file)
#         with open('frequency_test.csv', 'w', newline='') as csvfile:
#             fieldnames = ['result', 'construction_time', 'update_time', 'query_time', 'space_occupancy', 'true_result']
#             writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#             writer.writeheader()
#             for line in file:
#                 movieId, timestamp = line.strip().split(',')
#                 result = frequency_query(movieId, int(timestamp), initial_width=10000, depth=10)
#                 true_result = dic_frequency_query(int(movieId), int(timestamp))
#                 writer.writerow({
#                     'result': result[0],
#                     'construction_time': result[1],
#                     'update_time': result[2],
#                     'query_time': result[3],
#                     'space_occupancy': result[4],
#                     'true_result': true_result
#                 })
#
##topk
# if __name__ == "__main__":
#     with open('query.csv', 'r') as file:
#         next(file)
#         with open('topk_test.csv', 'w', newline='') as csvfile:
#             fieldnames = ['result', 'construction_time', 'update_time', 'query_time', 'space_occupancy', 'true_result']
#             writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#             writer.writeheader()
#             for line in file:
#                 movieId, timestamp = line.strip().split(',')
#                 result = top_k_query(10, int(timestamp))
#                 true_result = dic_top_k_query(10, int(timestamp))
#                 writer.writerow({
#                     'result': result[0],
#                     'construction_time': result[1],
#                     'update_time': result[2],
#                     'query_time': result[3],
#                     'space_occupancy': result[4]
#                 })



# member_query_data = [(1260, 1147877857), (2571, 1439472221), (96737, 1439474741), (63876, 1240952515),
#                      (400000, 1016738289), (1260, 10000000000), (1, 830000000), (2, 1600000000)]
#
# frequency_query_data = [(1260, 1147877857), (1, 1439472221), (140160, 1439474741), (63876, 1240952515)]
#
# top_k_query_data = [(10, 830786277), (10, 1016738289), (10, 1240952515), (10, 1573945484)]
#
# # # 成员查询测试
# print("成员查询测试：")
# true_query_count = 0
# for movieid, timestamp in member_query_data:
#     movieid = str(movieid)
#     result, construction_time, update_time, member_query_time, space_occupancy = member_query(movieid, timestamp,
#                                                                                               initial_width=10000,
#                                                                                               depth=10)
#     true_result = dic_member_query(movieid, timestamp)
#     if result == true_result:
#         true_query_count += 1
#     print(f"电影ID：{movieid}，时间戳：{timestamp}：测试答案：{result}\n正确答案：{true_result}")
#     print(
#         f"本次测试指标：\n此次成员查询时间：{member_query_time}\n构建时间：{construction_time}\n平均更新元素时间：{update_time}\n空间占用：{space_occupancy}")
#
#
# # 频度查询测试
# print("\n频度查询测试：")
# for movieid, timestamp in frequency_query_data:
#     movieid = str(movieid)
#     result, construction_time, update_time, frequency_query_time, space_occupancy = frequency_query(movieid, timestamp,
#                                                                                                     initial_width=10000,
#                                                                                                     depth=10)
#     true_result = dic_frequency_query(movieid, timestamp)
#     print(f"电影ID：{movieid}，时间戳：{timestamp}：测试答案：{result}\n正确答案：{true_result}")
#     print(
#         f"本次测试指标：\n此次频度查询时间：{frequency_query_time}\n构建时间：{construction_time}\n平均更新元素时间：{update_time}\n空间占用：{space_occupancy}")
#
# #Top-K查询测试
# print("\nTop-K查询测试：")
# for k, timestamp in top_k_query_data:
#     result, construction_time, update_time, top_k_query_time, space_occupancy = top_k_query(k, timestamp)
#     true_result = dic_top_k_query(k, timestamp)
#     print(f"Top-{k} 查询，时间戳：{timestamp}，结果：{result}\n正确答案：{true_result}")
#     print(
#         f"本次测试指标：\n此次TOPK查询时间：{top_k_query_time}\n构建时间：{construction_time}\n平均更新元素时间：{update_time}\n空间占用：{space_occupancy}")
