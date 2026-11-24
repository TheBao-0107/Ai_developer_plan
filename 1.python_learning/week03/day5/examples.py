from ..day4.examples import Restaurant


class IceCreamStand(Restaurant):
    """冰激凌小店类"""

    def __init__(self, restaurant_name, cuisine_type, flavors, number_served=0):
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavors = flavors

    def print_flavors(self):
        """显示所有冰激凌口味"""
        print(f"{self.flavors}")


iceCream_stand = IceCreamStand(
    "冰激凌店", "IceCream", ["melon", "strawberry", "blueberry", "orange"]
)
iceCream_stand.print_flavors()
