# 练习 2：累计支出小菜单。按 task.md 实现记一笔、查看累计、退出和无效选项提示，注意输入提示换行。
# 在下面写你的代码
flag = True
able_select_num_list = ["1", "2", "0"]
sum_money = 0
while flag:
    print("1. 记一笔 | 2. 查看累计 | 0. 退出")
    select_num = input("请选择：")
    if select_num not in able_select_num_list:
        print("无效选项")
        continue
    elif select_num == "1":
        money = int(input("请输入金额（正整数）："))
        sum_money += money
        print("已记录")
    elif select_num == "2":
        print(f"累计支出：{sum_money}元")
    elif select_num == "0":
        flag = False
        print("已退出")
