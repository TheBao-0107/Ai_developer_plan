# 练习 2：在检票台导入卧铺票类，打印新车票的票面。
# 在下面写你的代码
from ex1_tickets import SleeperTicket

if __name__ == "__main__":
    print("开始检票")
    print(SleeperTicket("昆明", "中铺").label())
