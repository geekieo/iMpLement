
# 总奖金 20.4。领取方案一：每年取0.68,取30年。领取方案二：一次性取出扣税后9.976。
# 奖金作为投资本金，每年有一定比例的增长，计算两种方案在 n 年后的资金总量。
def growth(captial, capital_increase=True, rate=1.04, year=30):
    if year <= 0:
        return 0
    
    cumulative_captial = captial
    if capital_increase:
        for i in range(year-1):
            cumulative_captial = (cumulative_captial + captial) * rate
    else:
        for i in range(year-1):
            cumulative_captial = cumulative_captial * rate
        # cumulative_captial = captial * （rate ** year)
    return cumulative_captial

def find_inflection(a, b, inflection_flag):
    if inflection_flag:
        if a>b:
            return True
    return False

if __name__ == "__main__":
    captial_peryear =  0.68
    captial_once = 9.976
    rate = 1.04 # 年增长率以年通胀率1.043为参考
    inflection_flag = True # 寻找拐点标记
    for year in range(30):
        peryear_final = growth(captial=captial_peryear, capital_increase=True, year=year)
        once_final = growth(captial=captial_once, capital_increase=False, year=year)
        if year > 0:
            print()
        print("每年循环增资{0}，年增长率{1}，{2}年后：{3:.2f}".format(captial_peryear, rate, year,peryear_final), end="\t")
        print("一次性投资{0}，年增长率{1}，{2}年后：{3:.2f}".format(captial_once, rate, year, once_final), end="\t")
        if find_inflection(peryear_final, once_final, inflection_flag):
            print("拐点", end="\t")
            inflection_flag = False