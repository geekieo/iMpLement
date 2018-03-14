class Sample:
    def __enter__(self):
        # 对象入口
        print("In __enter__()")
        # return "Foo"
        return self
 
    def __exit__(self, type, value, trace):
        # 如果对象存在异常，type, value, trace 返回异常信息
        print("In __exit__()")
        print("type:", type)
        print("value:", value)
        print("trace:", trace)

    def do_something(self):
        bar = 1/0 #此处应判别为除0异常
        return bar + 10
 
def get_sample():
    return Sample()

# 将 Sample().__enter__() 的返回值赋予 sample
with get_sample() as sample:
    # print("sample:", sample)
    sample.do_something()