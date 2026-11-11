# W2D3 练习 2：按类别汇总
# 具体要求、示例输出和验收清单见同目录 task.md。
# 在下面写你的代码
category_totals_dict = {"餐饮": [12, 18], "交通": [3], "学习": []}
for category, total in category_totals_dict.items():
    print(f"{category}：{len(total)}笔，共{sum(total)}元")
