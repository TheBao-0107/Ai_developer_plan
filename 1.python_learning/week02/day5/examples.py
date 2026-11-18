favorite_fruits = ["peach", "apple", "banana", "watermelon", "orange"]
fruit = input("请输入你最近最喜欢吃的水果：")
if fruit in favorite_fruits:
    print(f"You really like {fruit}")

river_dict = {"nile": "egypt", "changJiang": "China", "the yellow river": "China"}
for river, country in river_dict.items():
    print(f"The {river} runs through {country}")

pets = [
    {"category": "dog", "name": "Bobby", "master": "Bob"},
    {"category": "cat", "name": "Meow", "master": "Peter"},
    {"category": "pig", "name": "doundoun", "master": "Mark"},
]
for pet in pets:
    print(f"{pet['name']} is a {pet['category']}, his/her master is {pet['master']}")

flag = True
while flag:
    num_input = int(input("请输入你的数字（整数）："))
    if num_input % 2 == 0:
        print(f"{num_input}是偶数，程序退出")
        flag = False
    else:
        print(f"{num_input}是奇数，程序继续")
