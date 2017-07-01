class Desc:
    def __get__(self, ins, cls):
        print('self in Desc: %s ' % self )
        print(self, ins, cls)
    def prt(self):
        print('Desc.prt() print ', self)
class Test:
    x = Desc()
    def __get__(self, ins, cls):
        print('Test.__get__() print' , self)
    def prt(self):
        print('self in Test: %s' % self)
t = Test()
t.prt()
t.x
Test()