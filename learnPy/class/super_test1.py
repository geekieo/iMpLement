'''multiple inheritance 
super()方法 和 主动初始化父类 混用的不良结果
'''
class A(object):
    def __init__(self):
        print("enter A")
        print("leave A")
class B(object):
    def __init__(self):
        print("enter B")
        print("leave B")
class C(A):
    def __init__(self):
        print("enter C")
        super(C, self).__init__()
        print("leave C")
class D(A):
    def __init__(self):
        print("enter D")
        super(D, self).__init__()
        print("leave D")
class E(B, C):
    def __init__(self):
        print("enter E")
        B.__init__(self)
        C.__init__(self)
        print("leave E")
class F(E, D):
    def __init__(self):
        print("enter F")
        E.__init__(self)
        D.__init__(self)
        print("leave F")


f = F()