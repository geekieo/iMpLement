'''
description:划分数组
parameters:
    unsorted: 待划分数组
    low: 低位索引
    high: 高位索引
'''


def partition(unsorted, low, high):
    pivot = unsorted[low]
    while (low < high):
        while (unsorted[high] > pivot and low < high):
            high -= 1
        while (unsorted[low] <= pivot and low < high):
            low += 1
    unsorted[low] = pivot
    return low


def quick_sort(unsorted, low, high):
    loc = 0
    if (low < high):
        loc = partition(unsorted, low, high)
        quick_sort(unsorted, low, loc - 1)
        quick_sort(unsorted, loc + 1, high)


def __main__():
    x = [8, 5, 6, 4, 2, 3, 7, 9]
    quick_sort(x, 0, len(x))
    print(x)


__main__()