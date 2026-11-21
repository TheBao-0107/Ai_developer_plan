# 练习 1：用两种调用方式生成行李标签。
# 在下面写你的代码
def bag_tag(destination, number=1):
    """行李标签，接受信息，返回行李标签"""
    return f"{destination} · {number} 件"


tag1 = bag_tag("杭州")
print(tag1)

tag2 = bag_tag(number=3, destination="苏州")
print(tag2)
