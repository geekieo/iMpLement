'''
查看返回的闭包对象是什么
'''
def greeting_conf(prefix):
    def greeting(name):
        print(prefix, name)
    return greeting

mGreeting = greeting_conf("Good morning")

print(dir(mGreeting))
print(mGreeting.__closure__) #__closure__对应一个 tuple，包含一到多个cell对象
print(type(mGreeting.__closure__[0]))
print(mGreeting.__closure__[0].cell_contents)#cell内容为"Good morning""