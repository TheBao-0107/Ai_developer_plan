pets = [
    {"category": "dog", "name": "Bobby", "master": "Bob"},
    {"category": "cat", "name": "Meow", "master": "Peter"},
    {"category": "pig", "name": "doundoun", "master": "Mark"},
]
for pet in pets:
    print(f"{pet['name']} is a {pet['category']}, his/her master is {pet['master']}")

while input("请输入您的数字：") != "quit":
    print("输入有效")
print("输入为'quit'，程序退出")

labels = ["预览", "超时", "", "预览", "丢帧", "超时", "预览"]
appear_times = {}
for label in labels:
    if label:
        appear_times[label] = appear_times.get(label,0)+1
for k,v in appear_times.items():
    print(f"{k}：{v}")