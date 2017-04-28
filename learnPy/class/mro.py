import inspect
class D:
    pass

class C(D):
    pass

class B(D):
    pass

class A(B, C):
    pass

if __name__ == '__main__':
    print(inspect.getmro(A))
    