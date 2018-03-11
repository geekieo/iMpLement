class D:
    pass

class C(D):
    pass

class B(D):
    pass

class A(B, C):
    pass

if __name__ == '__main__':
    print(A.__mro__) #解析方法调用的顺序