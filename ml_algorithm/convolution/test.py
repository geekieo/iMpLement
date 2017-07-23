from convolution import Convolution


def test():
    c = Convolution()
    kernal =[[1,2,3], 
                [1,2,3],
                [1,2,3]]
    src=[[1,2,3,4,5,6,7,8],
        [1,2,3,4,5,6,7,8],
        [1,1,1,1,1,1,1,1],
        [2,2,2,2,2,2,2,2],
        [8,7,6,5,4,3,2,1],
        [1,0,1,0,1,0,1,0],
        [5,6,7,5,6,7,5,6],
        [1,1,1,0,0,0,2,2]]
    # for index,elem in enumerate(src):
    #     print(index,elem)
    dst1 = c.convolution(src, kernal)
    deKernal = c.transpose(kernal)
    dst2 = c.convolution(dst1, deKernal)
    print(src)
    print(dst2)

test()