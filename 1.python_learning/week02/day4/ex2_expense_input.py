# 练习 2：用 while 连续读取支出，遇到 q 结束；每笔保存为独立字典，输出明细和统计。
# 在下面写你的代码
money_list = []
sum_money = 0
while True:
    money = input("金额（正整数，q结束）：")
    money_num = 0
    if money == "q":
        break
    else:
        money_num = int(money)
        money_dict = {"amount": money_num}
        money_list.append(money_dict)
for index in range(len(money_list)):
    print(f"第{index + 1}笔：{money_list[index]['amount']}元")
    sum_money += money_list[index]["amount"]

print(f"共{len(money_list)}笔，总支出：{sum_money}元")
