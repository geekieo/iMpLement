"""
name: 最长回文字串 palindrome Manacher 算法
core princple：
    回文半径 = min(对称点回文半径，最长回文半径右边界) if 半径边界<最长回文半径右边界 
    else 在字符串长度范围内搜索回文
"""
def manacher(s):
    # step1: even to odd,  
    # princple: k -> 2k-1，
    # description: add '#' between each char, the count will always be odd
    s = '#'+'#'.join(s)+'#'

    # step2: search palindorme 
    lenth = len(s)
    radii=[-1]*lenth #存储每个字符的回文半径，初始化为-1表示未赋值
    posCenter = 0 #最右边界回文中心
    posRadius = 0 #最右边界回文半径

    for i in range(lenth):
        radii[i]=0 #初始化回文半径为0
        iMirror = 2*posCenter - i
        if i < posRadius:
            # 下面四句为 radii[i]=min(radii[iMirror], posRadius - i)
            if i+radii[iMirror] <= posRadius:
                radii[i] = radii[iMirror]
            else:
                radii[i] = posRadius - i
        #尝试扩展 i 点的回文半径，注意判断边界
        iLeft = radii[i]+1 #初始化扩展半径
        while i-iLeft>=0 and i+iLeft <=lenth-1 and s[i+iLeft]==s[i-iLeft]:
            radii[i]+=1
            iLeft +=1
        #更新最长回文中心和边界
        if radii[i]+i>posRadius:
            posCenter = i
            posRadius = radii[i]
    return radii



def test():
    s ="ajafajafb"
    RL = manacher(s)
    newRL= []
    # 提取原字符回文半径，经过加#处理后的回文半径=原字符串回文长度
    for i in range(len(RL)):
        if i%2==1:
            newRL.append(RL[i])
    print(newRL)

test()