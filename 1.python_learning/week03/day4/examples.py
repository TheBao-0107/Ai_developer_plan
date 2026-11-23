class Restaurant:
    """餐厅类"""

    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        """打印餐厅中的信息"""
        print(
            f"The restaurant name is {self.restaurant_name}, the cuisine type is {self.cuisine_type}"
        )

    def open_restaurant(self):
        """餐厅正在营业"""
        print("The restaurant is openning now")

    def set_number_served(self, number):
        """设置就餐人数"""
        self.number_served = number

    def increment_number_served(self, number):
        """让就餐人数递增"""
        self.number_served += number


restaurant = Restaurant("Test", "Hot", 1436)
print(
    f"There are {restaurant.number_served} people have been served in the restaurant which's name is {restaurant.restaurant_name}"
)
restaurant.number_served = 2000
print(
    f"There are {restaurant.number_served} people have been served in the restaurant which's name is {restaurant.restaurant_name}"
)
restaurant.set_number_served(50)
print(
    f"There are {restaurant.number_served} people have been served in the restaurant which's name is {restaurant.restaurant_name}"
)
restaurant.increment_number_served(50)
print(
    f"There are {restaurant.number_served} people have been served in the restaurant which's name is {restaurant.restaurant_name}"
)

restaurantA = Restaurant("餐厅A", "cuisineA")
restaurantA.describe_restaurant()
restaurantA.open_restaurant()

restaurantB = Restaurant("餐厅B", "cuisineB")

restaurantC = Restaurant("餐厅C", "cuisineC")

restaurantB.open_restaurant()
restaurantC.open_restaurant()

restaurantB.describe_restaurant()
restaurantC.describe_restaurant()


class User:
    """用户类"""
    def __init__(self, first_name, last_name, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

    def describe_user(self):
        """打印用户信息摘要"""
        print(f"my name is {self.first_name} {self.last_name}")

    def greet_user(self):
        """向用户发出个性化的问候"""
        print(f"Hello,{self.first_name} {self.last_name}!!!")

    def increment_login_attempts(self):
        """增加一次尝试次数"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """重置尝试次数"""
        self.login_attempts = 0

bao = User("bao", "zheng")
yu = User("cheng", "yu")

bao.describe_user()
bao.greet_user()

yu.greet_user()
yu.describe_user()

bao.increment_login_attempts()
bao.increment_login_attempts()
bao.increment_login_attempts()
bao.increment_login_attempts()
bao.increment_login_attempts()
bao.increment_login_attempts()
bao.increment_login_attempts()
bao.increment_login_attempts()
bao.increment_login_attempts()
bao.increment_login_attempts()
bao.increment_login_attempts()
print(f"bao has attempted for {bao.login_attempts} times")
bao.reset_login_attempts()
print(f"bao has attempted for {bao.login_attempts} times")