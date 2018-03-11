import inspect

class D:
    pass
class B(D):
    pass
class E:
    pass
class C(E):
    pass
class A(B, C):
    pass

if __name__ == '__main__':
    print(inspect.getmro(A)) #元组形式返回A类的基类（包括A类），以method resolution顺序;通常A类为第一个元素
    print(A.__mro__)