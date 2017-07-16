nums = [3, 2, 8, 0, 1]
print(sorted(nums))

score = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_score(t):
    return t[1]


def by_name(t):
    return t[0]


print(sorted(score, key=by_score))
