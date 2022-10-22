# list comprehansive
n = 8                      # 全局变量
class Chess:
    # 类变量
    n = 4                   # 只能被 list comprehansive 第一层 for 循环读取到
    position = [
        (i,j)
        for i in range(n)   # list comprehansive 第一层 range() 的 n 拿的是类命名空间的 n 对应的常量，否则取全局变量
        for j in range(n)   # list comprehansive 多层 range() 的 n 和第一层 n 不在同一个 frame 中执行，这里的 n 读取的是全局变量 n
    ]
    position_oldschool = []
    for i in range(n):
        for j in range(n):
            position_oldschool.append((i,j))


    def __init__(self) -> None:
        # 实例变量
        self.n=2         
        self.position_init = [
            (i,j)
            for i in range(self.n)   
            for j in range(self.n)   
        ]

c = Chess()
# print(Chess.n)
print(c.position)
print(c.position_oldschool)
print(c.position_init)

Chess.n = 1
c = Chess()
print(Chess.n)
print(c.position)
print(c.position_oldschool)
print(c.position_init)