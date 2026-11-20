# 换乘还剩几分钟：用函数计算两趟车各自的等待时间。
# 在下面写你的代码
def transfer_time(busTime,walkTime):
    """计算到下一站之后要等多久"""
    return busTime-walkTime

print(f"第一趟还需等 {transfer_time(24,9)} 分钟")
print(f"第二趟还需等 {transfer_time(8,8)} 分钟")