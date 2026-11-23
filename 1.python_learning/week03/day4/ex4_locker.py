# 可选挑战：尝试连续存包，记录寄存柜的剩余空格数。
# 在下面写你的代码
class Locker:
    """寄存柜类"""

    def __init__(self, number):
        self.empty_number = number

    def save_package(self):
        """存包方法"""
        if self.empty_number > 0:
            self.empty_number -= 1
            return "已存入"
        else:
            return "已满"


test_locker = Locker(1)
print(f"{test_locker.save_package()}，剩余 {test_locker.empty_number} 格")
print(f"{test_locker.save_package()}，剩余 {test_locker.empty_number} 格")
