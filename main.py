# Sorting algorithms with decorator for calculate execution time
import time
import random


def deco(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print(f'Execution time sorting algorithm by select - {time.time() - start}')

    return wrapper


def find_smallest(arr):
    sm_number = arr[0]
    sm_index = 0
    for i in range(1, len(arr)):
        if arr[i] < sm_number:
            sm_number = arr[i]
            sm_index = i
    return sm_index


#  Sorting list by select
@deco
def sorting(arr):
    global sorted_arr
    for i in range(len(arr)):
        sorted_arr.append(arr.pop(find_smallest(arr)))
    return sorted_arr


if __name__ == '__main__':
    sorted_arr = []
    arr = [random.randint(1, 100) for _ in range(10000)]
    sorting(arr)
    print(sorted_arr)
