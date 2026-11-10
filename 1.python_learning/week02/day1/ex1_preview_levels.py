# W2D1 练习 1：预览耗时分级（基础）
# 按 task.md 的数据和规则，用循环及条件分支输出每次预览耗时的等级。
# 在下面写你的代码
time_costs = [15, 16, 17, 33, 34]
for time_cost in time_costs:
    if time_cost <= 16:
        print(f"{time_cost} ms：流畅")
    elif time_cost <= 33:
        print(f"{time_cost} ms：需关注")
    else:
        print(f"{time_cost} ms：卡顿")
