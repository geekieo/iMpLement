"""
快速排序
"""


def partition(unsorted, low, high):
    '''
    description: 划分数组
    parameters:
        unsorted: 待划分数组
        low: 低位索引
        high: 高位索引
    return:
        根据基准值 pivot 交换后的 pivot 索引
    '''
    pivot = unsorted[low]  #pivot 分割基准值
    init_index = low  #pivot 的初始下标索引
    while (low < high):
        while (unsorted[high] > pivot and low < high):
            high -= 1
        while (unsorted[low] <= pivot and low < high):
            low += 1
        # 一轮比完，置换哨兵值位置，实现遍历过地部分左小右大
        if (unsorted[low] != unsorted[high]):
            unsorted[low], unsorted[high] = unsorted[high], unsorted[low]
    # 小值区间的最后一个值和 pivot 置换位置，完成分割
    if (pivot != unsorted[low]):
        # 注意！这种写法交换的是成员指针，不能直接用 pivot 替换 unsorted[init_index]，不在一个数组中无法交换
        unsorted[init_index], unsorted[low] = unsorted[low], unsorted[
            init_index]
    return low  #此时 low == high


def quick_sort(unsorted, low, high):
    loc = 0  # pivot 索引变量
    if (low < high):
        loc = partition(unsorted, low, high)
        quick_sort(unsorted, low, loc - 1)
        quick_sort(unsorted, loc + 1, high)


def __main__():
    x = [8, 5, 6, 4, 2, 3, 7, 9]
    quick_sort(x, 0, len(x) - 1)
    print(x)


__main__()