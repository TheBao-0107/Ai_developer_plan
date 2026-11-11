# W2D3 可选挑战：预算余额
# 具体要求、示例输出和验收清单见同目录 task.md。
# 在下面写你的代码
budget_balance = {
    "餐饮": {"budget": 40, "spent": 30},
    "交通": {"budget": 10, "spent": 3},
}
budget_balance["餐饮"]["spent"] = 36
for category, blance in budget_balance.items():
    print(
        f"{category}：剩余{budget_balance[category]['budget'] - budget_balance[category]['spent']}元"
    )
