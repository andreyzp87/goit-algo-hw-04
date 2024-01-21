import random
from timeit import timeit


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи,
    # додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def main():
    test_arrays = {
        'Small': [random.randint(0, 100) for _ in range(100)],
        'Medium': [random.randint(0, 100) for _ in range(1000)],
        'Large': [random.randint(0, 100) for _ in range(10000)]
    }

    print(f"{'| Algorithm ': <18} | {'Time (ms) ': <22} | {'Size': <10} |")

    for size, arr in test_arrays.items():
        result = {
            'Merge Sort': timeit(lambda: merge_sort(arr.copy()), number=10),
            'Insertion Sort': timeit(lambda: insertion_sort(arr.copy()), number=10),
            'Timsort': timeit(lambda: sorted(arr), number=10)
        }
        for algo, time in result.items():
            print(f"| {algo: <16} | {time: <22} | {size: <10} |")
        print(f"| {'-' * 16} | {'-' * 22} | {'-' * 10} |")


if __name__ == '__main__':
    main()
