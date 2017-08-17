"""
现在有一个数组，已知一个数出现的次数超过了一半，请用O(n)的复杂度的算法找出这个数
"""
def search(inArray):
    '''
    找出数组中数量超过一半的数
    '''
    size = len(inArray)
    count = 0
    current = inArray[0]
    for i in range(size):
        if count == 0:
            current = inArray[i]
            count = 1
        else:
            if inArray[i]==current:
                count += 1
            else:
                count -= 1
    return current

def test():
    a = [1,1,1,1,2,2,2]
    b = [3,3,3,3,3,4,4,4,4]
    c = [5,5,5,5,6,6,6,6,6]
    print(search(a))
    print(search(b))
    print(search(c))

test()