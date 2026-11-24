# 练习 1：让普通车票和卧铺票各自给出票面文字。
# 在下面写你的代码
class Ticket:
    """车票类"""

    def __init__(self, destination):
        self.destination = destination

    def label(self):
        """返回目的地的票面文字"""
        return f"目的地：{self.destination}"


class SleeperTicket(Ticket):
    """卧铺票类"""

    def __init__(self, destination, place):
        super().__init__(destination)
        self.place = place

    def label(self):
        """返回目的地的票面文字"""
        return f"目的地：{self.destination}｜{self.place}"


if __name__ == "__main__":
    print(Ticket("苏州").label())
    print(SleeperTicket("成都", "下铺").label())
