'''
闭包只是在表现形式上跟函数类似，但实际上不是函数。
闭包 greeting_conf() 在运行时可以有多个实例，
不同的引用环境（prefix 变量）和相同的函数（greeting)组合
可以产生不同的实例（id）
'''


def greeting_conf(prefix):
    def greeting(name):
        print(prefix, name)

    return greeting


mGreeting = greeting_conf("Good morning")
print("function name is:", mGreeting.__name__,
    ". type is:", type(mGreeting))
print("id of mGreeting is:", id(mGreeting))

aGreeting = greeting_conf("Good afternoon")
print("function name is:", aGreeting.__name__)
print("id of mGreeting is:", id(aGreeting))
