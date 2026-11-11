# W2D3 练习 1：三笔生活账
# 具体要求、示例输出和验收清单见同目录 task.md。
# 在下面写你的代码
daily_records_list = [
    {"date": "2026-11-11", "category": "餐饮", "amount": 12, "note": "早餐"},
    {"date": "2026-11-11", "category": "交通", "amount": 3},
]
daily_records_list.append(
    {"date": "2026-11-11", "category": "餐饮", "amount": 18, "note": "晚餐"}
)
print("账目明细")
sum_amount = 0
for record in daily_records_list:
    print(
        f"{record['date']} | {record['category']} | {record['amount']}元 | {record.get('note', '无备注')}"
    )
    sum_amount += record.get("amount", 0)
print(f"共{len(daily_records_list)}笔")
print(f"总支出：{sum_amount}元")
