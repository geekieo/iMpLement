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
    print(A.__mro__)