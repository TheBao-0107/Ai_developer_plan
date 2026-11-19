# W2D6：按 day6/task.md 完成记账本菜单、记一笔、查看全部和退出，保存每笔账的金额、类别、备注、日期。
# 在下面写你的代码
ledger_list = []
flag = True
while flag:
    print("1. 记一笔 | 2. 查看全部 | 4. 退出")
    select_num = input("请选择：\n")
    if select_num == "1":
        ledger = {"amount": 0, "category": "", "note": "", "date": ""}
        ledger["amount"] = int(input("请输入金额（正整数）:\n"))
        ledger["category"] = input("请输入类别：\n")
        ledger["note"] = input("请输入备注：\n")
        ledger["date"] = input("请输入日期（YYYY-MM-DD）：\n")
        ledger_list.append(ledger)
        print("已记录")
    elif select_num == "2" and len(ledger_list) == 0:
        print("暂无记录")
    elif select_num == "2" and len(ledger_list) != 0:
        for index in range(len(ledger_list)):
            print(
                f"{index + 1}. {ledger_list[index]['date']} | {ledger_list[index]['category']} | {ledger_list[index]['amount']}元 | {ledger_list[index]['note']}"
            )
        print(f"共{len(ledger_list)}笔")
    elif select_num == "4":
        flag = False
        print("已退出")
    else:
        print("无效选项")
