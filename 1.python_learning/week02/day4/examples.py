carBrand = input("请输入您要租赁的汽车品牌：")
print(f"Let me see if I can find you a {carBrand}")

custom_num = int(input("请输入您的用餐人数："))
if custom_num > 8:
    print("对不起，当前没有空桌了")
else:
    print("欢迎光临！")

num_input = int(input("请输入一个整数："))
if num_input % 10 == 0:
    print("输入的数是10的整数倍")
else:
    print("输入的数不是10的整数倍")

food = input("请输入披萨配料：")
while food != "quit":
    print(f"在披萨中添加{food}")
    food = input("请输入披萨配料：")

flag = True
while flag:
    food = input("请输入披萨配料：")
    if food == "quit":
        flag = False
    else:
        print(f"在披萨中添加{food}")

while True:
    food = input("请输入披萨配料：")
    if food == "quit":
        break
    else:
        print(f"在披萨中添加{food}")

while True:
    age_num = int(input("请输入您的年龄："))
    if age_num < 3:
        print("您免费")
        break
    elif age_num < 12:
        print("您的票价是10美元")
    else:
        print("您的票价是15美元")

sandwich_orders = ["big", "good", "nice", "champion", "wesli", "nice", "nice", "nice"]
finished_sandwiches = []
while sandwich_orders:
    print(f"I made {sandwich_orders[0]} sandwich")
    finished_sandwiches.insert(0, sandwich_orders.pop())
print(finished_sandwiches)

print("不好意思，nice三明治卖完了")
while "nice" in finished_sandwiches:
    finished_sandwiches.remove("nice")
print(finished_sandwiches)
