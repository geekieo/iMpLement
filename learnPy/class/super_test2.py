class A(object):
    def go(self):
        print("go A go!")
    def stop(self):
        print("stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")

class B(A):
    def go(self):
        super(B, self).go()
        print("go B go!")

class C(A):
    def go(self):
        super(C, self).go()
        print("go C go!")
    def stop(self):
        super(C, self).stop()
        print("stop C stop!")

class D(B,C):
    def go(self):
        super(D, self).go()
        print("go D go!")
    def stop(self):
        super(D, self).stop()
        print("stop D stop!")
    def pause(self):
        print("wait D wait!")

class E(B,C): pass

def task(message):
    a = A()
    b = B()
    c = C()
    d = D()
    e = E()
    if message == 'go':
        a.go()
        b.go()
        c.go()
        d.go()
        e.go()
    elif message =='stop':
        a.stop()
        b.stop()
        c.stop()
        d.stop()
        e.stop()
    elif message == 'pause':
        a.pause()
        b.pause()
        c.pause()
        d.pause()
        e.pause()

def userInterface():
    while 1:
        message = input('enter \'go\' \'stop\' \'pause\' to run test, enter \'q\' to exit:\r\n')
        if message =='q':
            break
        else:
            task(message)


if __name__ =="__main__":
    userInterface();