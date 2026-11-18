# 练习 1：筛选旅途交通账。按 task.md 保存账目，输出交通明细、笔数和总额，处理缺少备注的情况。
# 在下面写你的代码
money_list = [
    {"category": "交通", "amount": 6, "note": "地铁"},
    {"category": "餐饮", "amount": 24, "note": "午饭"},
    {"category": "交通", "amount": 4},
    {"category": "购物", "amount": 15, "note": "明信片"},
]
sum_traffic_money = {"次数": 0, "总花费": 0}
for money in money_list:
    if money.get("category") == "交通":
        print(
            f"{money.get('category')}：{money.get('amount')}元，{money.get('note', '未备注')}"
        )
        sum_traffic_money["次数"] += 1
        sum_traffic_money["总花费"] += money.get("amount", 0)
print(f"交通合计：{sum_traffic_money['次数']}笔，{sum_traffic_money['总花费']}元")
