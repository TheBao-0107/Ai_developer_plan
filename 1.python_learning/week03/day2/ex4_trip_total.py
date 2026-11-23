# 可选挑战：计算任意笔车费和带名称的附加费用的总额。
# 在下面写你的代码
def trip_total(*current_money, **extra_money_info):
    """返回所有金额之和"""
    sum_money = 0
    for money in current_money:
        extra_money_info["current_trip_money"] = (
            extra_money_info.get("current_trip_money", 0) + money
        )
    for v in extra_money_info.values():
        sum_money += v
    return sum_money


print(trip_total(12, 8, locker=7))
print(trip_total(parking=9))
print(trip_total())
