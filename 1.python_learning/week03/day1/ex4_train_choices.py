# 哪趟车来得及（可选）：用函数判断能否赶上各趟车，输出赶得上的车次。
# 在下面写你的代码
def is_train_in_time(departure_time, walk_time):
    """判断是否能赶上这趟车"""
    return walk_time <= departure_time


train_departure_time_list = [8, 12, 19]
walk_time = 12

for time in train_departure_time_list:
    if is_train_in_time(time, walk_time):
        print(f"{time} 分钟后发车")
