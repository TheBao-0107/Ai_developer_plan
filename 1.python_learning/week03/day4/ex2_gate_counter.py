# 练习 2：分别记录两个闸口的放行人数。
# 在下面写你的代码
class GateCounter:
    """闸口计数类"""

    def __init__(self, name, number=0):
        self.name = name
        self.number = number

    def let_go(self, num):
        """接受本次通过的人数，累加到闸口记录中"""
        self.number += num


if __name__ == "__main__":
    counter_east = GateCounter("东门")
    counter_west = GateCounter("西门")
    counter_east.let_go(3)
    counter_east.let_go(2)
    print(f"{counter_east.name} {counter_east.number} 人")
    print(f"{counter_west.name} {counter_west.number} 人")
    counter_west.let_go(1)
    print(f"{counter_east.name} {counter_east.number} 人")
    print(f"{counter_west.name} {counter_west.number} 人")
