"""
name: 最长回文字串 palindrome Manacher 算法
core princple：
    回文半径 = min(对称点回文半径，最长回文半径右边界) if 半径边界<最长回文半径右边界 
    else 在字符串长度范围内搜索回文
"""
def manacher(s):
    radii=[-1]*len(s) #存储每个字符的回文半径
    maxRadius = 0 #最长回文右边界

    # step1: even to odd,  
    # princple: k -> 2k-1，
    # description: add '#' after every char, delete the last one，
    s = '#'.join(s)
    print(s)
    print(radii)


def test():
    s ="ajafajafb"
    manacher(s)
    # RL = manacher(s)
    # newRL= []
    # for i in range(len(RL)):
    #     if i%2==1:
    #         newRL.append(RL[i])
    # print(newRL)

test()