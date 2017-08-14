'''
闭包（Closure）是词法闭包（Lexical Closure）的简称，是引用了自由变量的函数。
这个被引用的自由变量将和这个函数一同存在，即使已经离开了创造它的环境也不例外。
所以，闭包是由函数和与其相关的引用环境组合而成的实体。

Python中通过提供 namespace 来实现重名函数/方法、变量等信息的识别，
其一共有三种 namespace，分别为：

local namespace: 作用范围为当前函数或者类方法
global namespace: 作用范围为当前模块
build-in namespace: 作用范围为所有模块
当函数/方法、变量等信息发生重名时，Python会按照：
    “local namespace -> global namespace -> build-in namespace”
的顺序搜索用户所需元素，并且以第一个找到此元素的 namespace 为准。

同时，Python中的内建函数locals()和globals()可以用来查看不同namespace中定义的元素。
'''

s = "string in global"
num = 99

def numFunc(a,b):
    num = 100
    print("pirnt s in numFunc",s)

    def addFunc(a,b):
        s="stirng in addFunc"
        print("print s in addFunc:",s)
        print("print num in addFunc:",num)
        print("locals of addFunc:", locals())
        print("%d + %d = %d" %(a,b,a+b))
        return a+b
        
    print("locals of numFunc:", locals())
    
    print(addFunc(a,b))

numFunc(3,6)
print("globals:", globals())

        