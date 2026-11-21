from module import func_print

test_list = ["1", "2", "3", "4", "a", "b"]


def show_messages(message_list):
    """打印列表中的所有消息"""
    for message in message_list:
        print(message)


show_messages(test_list)
sent_messages = []


def send_messages(original_list, sent_messages_list):
    """将原始列表中的消息全部挪到sent_messages_list中并打印"""
    while original_list:
        message = original_list.pop()
        sent_messages.append(message)
        print(message)


print(test_list)
print(sent_messages)
send_messages(test_list[:], sent_messages)
print(test_list)
print(sent_messages)


def sandwich_made(*foods):
    """打印制作三明治的食材清单"""
    print("Let's make sandwich with these foods")
    for food in foods:
        print(f"- {food}")


sandwich_made("pineapple")
sandwich_made("cola", "meat")
sandwich_made("cola", "meat", "beaf", "fish")


def build_profile(first, last, **user_info):
    """创建⼀个字典，其中包含我们知道的有关⽤户的⼀切"""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


my_user_profile = build_profile(
    "bao", "zheng", location="China", company="Alibaba", Hate="Huawei"
)
print(my_user_profile)


def car_dict(made, id, **info):
    """将一辆汽车的信息存在一个字典中"""
    info["made"] = made
    info["id"] = id
    return info


car = car_dict("BWM", "111", color="white", drive="4wheeldrive", money="40w")
print(car)

# module.func_print('你好啊')
func_print("你好啊")
