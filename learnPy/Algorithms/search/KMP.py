# Knuth-Morris-Pratt字符串查找算法
# 在一个字符串 S 内查找一个词 W 的出现位置，计算复杂度O(n)

def match(s,q):
    """
    Args:
        s: input stirng
        q: pattern to search
    KMP(Knuth-Morris-Pratt)
        * Fast Pattern Matching in Strings (SIAM '77)
        * Guaranteed worst case performance: O(m+n)
            ** Two stages:
                *** Pre-processing: next table building from pattern O(m) 
                *** Matching: O(n)
            ** Space complexity: O(m)
    Analysis
        Match
        * case 1: s[i] ==  p[j], match
            ** Action: ++i, ++j: try next pair
        * case 2: s[i] !=  p[j], mismatch
            ** Key idea: use partial matching information
            ** Let q = p[0~j-1] be the partial matched string
            ** Action: i remains the same, if j == 0: ++i else j = next[j] 

    """
    ans = []                # 匹配下标
    next = build(p)         # 匹配串的前后缀最长匹配表

    # build next table

    # matching



if __name__ == "__main__":
    s = "babc ababa cabababcda"
    q = "abababcd"
    match(s, q)