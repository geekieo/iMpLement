"""
查找第k个数
快排划分
"""


def partition(unsorted, low, high):
    #取中间位置(或中间偏左位置)为基准值
    init = int((low + high) / 2)
    #以unsorted[init]为基准值，左小右大交换
    while (low < high):
        while (unsorted[high] > unsorted[init] and low < high):
            high -= 1
        while (unsorted[low] <= unsorted[init] and low < high):  #相等的值会跳过
            low += 1
        unsorted[low], unsorted[high] = unsorted[high], unsorted[low]
    #经过上面交换，此时 low=high，pivot 从起始位置交换到该位置
    if (unsorted[low] != unsorted[init]):
        unsorted[low], unsorted[init] = unsorted[init], unsorted[low]
    return low  #返回基准值置换位置


def quick_search(unsorted, low, high):
    '''
    “随机”选择基准值，这里选择区间中间值（中间偏左值）
    使用快排划分法，以基准为中心，分成左小右大，
    递归，直到dst_index的值置换到正确位置
    '''
    loc_index = -1
    global find  #声明可修改的全局变量
    if (low == high):  #进入递归时找到
        find = True
        return
    while (low < high):
        loc_index = partition(unsorted, low, high)  #左小右大划分后的基准值下标索引
        if (loc_index > dst_index):
            quick_search(unsorted, low, loc_index - 1)  #进入递归，high索引-1
            if (find == True): return  #跳出递归
        elif (loc_index < dst_index):
            quick_search(unsorted, loc_index + 1, high)  #进入递归，low索引+1
            if (find == True): return  #跳出递归
        elif (loc_index == dst_index):  #partition 后直接找到
            find = True  #设置跳出标识符
            return


#全局变量
find = False  #递归跳出标记，需局部修改
dst_index = 7  #目标位置，不用局部修改


if __name__ == "__main__":
    #x = [5, 4, 3, 9, 7, 8, 2, 1, 3]
    x = [5, 4, 3, 7, 8, 2, 1, 3]
    #x=[6,6,3,4,4,4,4,5,1,1,1]
    length = len(x)
    #此处需入参范围校验
    quick_search(x, 0, length - 1)
    print(x[dst_index])