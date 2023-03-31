# Sorting algorithms with decorator for calculate execution time
import time
import random
# import colorama


# Decorator for checking execution time
def deco(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f'execution time = {time.time() - start} second')
        return result

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
def sorted_by_select(arr):
    sorted_arr = []
    # colorama.init()
    xx = len(arr)
    for i in range(xx):
        # Progress bar
        # print(f'\r\033[KNumber {i} of {xx}', end='')
        sorted_arr.append(arr.pop(find_smallest(arr)))
    print()
    print(f'Sorting algorithm by select  for {elements} pieces: ', end='')

    return sorted_arr


# Bubble sort
@deco
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    print(f'The bubble sorting algorithm for {elements} pieces: ', end='')
    return arr


def gen_arr(elements=1000):
    arr = [random.randint(1, 100) for _ in range(elements)]
    return arr


if __name__ == '__main__':
    elements = 10000
    sorted_by_select(gen_arr(elements))
    bubble_sort(gen_arr(elements))
