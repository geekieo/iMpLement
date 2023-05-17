
# 总奖金 20.4。领取方案一：每年取0.68,取30年。领取方案二：一次性取9.976。
def growth(captial, capital_increase=True, rate=1.04, year=30):
    if year <= 1:
        return captial
    
    cumulative_captial = captial
    if capital_increase:
        for i in range(year-1):
            cumulative_captial += (cumulative_captial + captial) * rate
    else:
        for i in range(year-1):
            cumulative_captial += cumulative_captial * rate
        # cumulative_captial = captial * rate ** year      
    return cumulative_captial

if __name__ == "__main__":
    captial_peryear =  0.68
    captial_once = 9.976
    rate = 1.04 # 年增长率以年通胀率1.043为参考
    year = 2
    print("每年取出{0}，每年循环增资，年增长率{1}，{2}年后：".format(captial_peryear, rate, year),
          growth(captial=captial_peryear, capital_increase=True, year=year))
    print("一次性取出{0}，一次性投资，年增长率{1}，{2}年后：".format(captial_once, rate, year),
          growth(captial=captial_once, capital_increase=False, year=year))
    