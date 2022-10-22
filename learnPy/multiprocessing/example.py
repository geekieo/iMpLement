import multiprocessing
import os

print(os.getpid())

def f():
    print(os.pid())
    
# 使用方法一
p = multiprocessing.Process(target=f)
p.start()
p.join()

# 使用方法二
class MyProcess(multiprocessing.Process):
    def run(self):
        f()

p = MyProcess()
p.start()
p.join()
