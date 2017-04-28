class A(object):
    pass

class B(object):
    pass

class C(A, B):
    pass

class D(B, A):
    pass

class E(C, D):
    pass

if __name__ == '__main__':
    print(E.__mro__)