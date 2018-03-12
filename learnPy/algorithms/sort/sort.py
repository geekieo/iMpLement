nums = [3, 2, 8, 0, 1]
print(sorted(nums))

################################

score = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_score(t):
    return t[1]


def by_name(t):
    return t[0]


print(sorted(score, key=by_score))

#####################

elem = [(2,11,"A"),(1,11,"D"),(1,3,"C"),(2,4,"B")]
print(elem)
print(sorted(elem))
# lambda 函数返回新的元组
print(sorted(elem,key = lambda e:(e[1],e[0])))