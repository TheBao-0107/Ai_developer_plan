# W1D5 练习 1：相机耗时小报告，具体要求和示例输出见同目录 task.md。
# 按采集顺序保存 42、30、36、52 毫秒，计算平均耗时并保留原始顺序。
# 取得按耗时升序排列的最快两次，用循环逐条输出；自查变量命名。
# 在下面写你的代码
list_report_time_cost = [42, 30, 36, 52]
average_time_cost = sum(list_report_time_cost) / len(list_report_time_cost)
sorted_list_report_time_cost = sorted(list_report_time_cost)
fatestTwo = sorted_list_report_time_cost[:2]
print(f"原始耗时：{list_report_time_cost} ms")
print(f"平均耗时：{average_time_cost} ms")
print(f"最快两次：{fatestTwo} ms")
print(f"逐条查看：")
for timeCost in fatestTwo:
    print(f"{timeCost} ms")