import numpy as np


class CountMinSketch:
    def __init__(self, initial_width, depth, fill_ratio_threshold=0.8):
        self.width = initial_width
        self.depth = depth
        self.counters = np.zeros((depth, initial_width), dtype=int)
        self.fill_ratio_threshold = fill_ratio_threshold

    def increment(self, key):
        if self.fill_ratio() > self.fill_ratio_threshold:
            self.expand()
        for i in range(self.depth):
            hash_val = hash(str(i) + key) % self.width
            self.counters[i, hash_val] += 1

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
    count_min_sketch = CountMinSketch(initial_width, depth, fill_ratio_threshold)
    with open('ratings.csv', 'r') as file:
        next(file)
        for line in file:
            _, movie, _, time = line.strip().split(',')
            if int(time) <= timestamp:
                count_min_sketch.increment(movie)

    flag = False
    if count_min_sketch.estimate(movieId) > 0:
        flag = True
    return flag


def frequency_query(movieId, timestamp, initial_width, depth, fill_ratio_threshold=0.8):
    count_min_sketch = CountMinSketch(initial_width, depth, fill_ratio_threshold)
    with open('ratings.csv', 'r') as file:
        next(file)
        for line in file:
            _, movie, _, time = line.strip().split(',')
            if int(time) <= timestamp:
                count_min_sketch.increment(movie)

    freq = count_min_sketch.estimate(movieId)
    if freq == 'inf':
        freq = 0
    return freq


def top_k_query(k, timestamp):
    misra_gries = MisraGries(k)
    with open('ratings.csv', 'r') as file:
        next(file)
        for line in file:
            _, movie, _, time = line.strip().split(',')
            if int(time) <= timestamp:
                misra_gries.process_item(movie)
    top_k_items = misra_gries.get_top_k()
    return top_k_items


def main():
    while True:
        print("请选择查询功能：\n1. 成员查询\n2. 频度查询\n3. Top-k 查询")
        choice = input("请输入查询功能选项 (1-3): ")

        if choice not in ['1', '2', '3']:
            print("请选择有效的选项 (1-3)！")
            continue
        if choice == '1' or choice == '2':
            movieId = input("请输入电影 ID: ")
            timestamp = int(input("请输入时间戳: "))
            if choice == '1':
                result = member_query(movieId, timestamp, initial_width=10000, depth=10)
                if result:
                    print(f"电影 {movieId} 在时间戳 {timestamp} 及之前被评分过。")
                else:
                    print(f"电影 {movieId} 在时间戳 {timestamp} 及之前未被评分过。")
            elif choice == '2':
                frequency = frequency_query(movieId, timestamp, initial_width=10000, depth=10)
                print(f"电影 {movieId} 在时间戳 {timestamp} 及之前被评分的总次数为: {frequency}")
        elif choice == '3':
            k = int(input("请输入要查询的前 k 个电影数目: "))
            timestamp = int(input("请输入时间戳: "))
            top_k_items = top_k_query(k, timestamp)
            print(f"时间戳 {timestamp} 及之前被评分次数最多的前 {k} 个电影:")
            for i, (movie, count) in enumerate(top_k_items, start=1):
                print(f"{i}. 电影 ID: {movie}, 评分次数: {count}")

        another_query = input("是否继续进行其他查询？(yes/no): ")
        if another_query.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
