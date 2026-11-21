# 练习 2：把物品加入传入的随身包清单，在调用处查看清单。
# 在下面写你的代码
current_packing_list = ["车票"]


def packing_list(current_list, thing):
    """接受现有的清单和一个物品，将该物品加到现有清单列表末尾"""
    current_list.append(thing)


packing_list(current_packing_list, "水杯")
print(current_packing_list)
packing_list(current_packing_list, "雨伞")
print(current_packing_list)
