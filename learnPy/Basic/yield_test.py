def getValue(a):
    length = len(a)
    i=0
    while True:
        if (i>length-1):
            return
        b = a[i]
        yield b
        i += 1

if __name__ == "__main__":
    a=[1,2,3,4]
    p = getValue(a)
    print(next(p))
    print(next(p))
    print(next(p))
    print(next(p))
    print(next(p))