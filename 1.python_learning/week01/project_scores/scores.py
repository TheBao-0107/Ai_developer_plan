# W1D6：成绩统计程序（上）。完整题目见 ../day6/task.md。
# 保存 10 个分数，计算人数、平均分、最高分、最低分，降序输出并保留原始顺序。
# W1D7：在本文件继续统计及格人数、逐行展示成绩，完整题目见 ../day7/task.md。
# 在下面写你的代码
score_list = [88, 59, 76, 100, 60, 92, 45, 83, 60, 97]
num_students = len(score_list)
average_score = sum(score_list)/num_students
max_score = max(score_list)
min_score = min(score_list)
sorted_score_list = sorted(score_list,reverse=True)
print(f"=== 成绩统计（上） ===")
print(f"原始成绩：{score_list}")
print(f"人数：{num_students}")
print(f"平均分：{average_score}")
print(f"最高分：{max_score}")
print(f"最低分：{min_score}")
print(f"降序成绩：{sorted_score_list}")