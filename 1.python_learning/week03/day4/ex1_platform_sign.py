# 练习 1：创建站台换乘牌，改站台后再次显示牌面。
# 在下面写你的代码
class PlatformSign:
    """换乘牌类"""

    def __init__(self, destination, id):
        self.destination = destination
        self.id = id

    def text_sign(self):
        """返回一行可直接打印的牌面文字"""
        return f"{self.destination} · {self.id} 号站台"


if __name__ == "__main__":
    sign_test = PlatformSign("杭州东", 3)
    print(sign_test.text_sign())

    sign_test.id = 5
    print(sign_test.text_sign())
