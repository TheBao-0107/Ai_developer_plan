# 保存 10 个分数，计算人数、平均分、最高分、最低分，降序输出并保留原始顺序。
# 在下面写你的代码
score_list = [88, 59, 76, 100, 60, 92, 45, 83, 60, 97]
num_students = len(score_list)
average_score = sum(score_list)/num_students
max_score = max(score_list)
min_score = min(score_list)
sorted_score_list = sorted(score_list,reverse=True)
print(f"=== 成绩统计报告 ===")
print(f"原始成绩：{score_list}")
print(f"人数：{num_students}")
print(f"平均分：{average_score}")
print(f"最高分：{max_score}")
print(f"最低分：{min_score}")
# print(f"降序成绩：{sorted_score_list}")
num_passed = 0
for score in score_list:
    if(score >= 60):
        num_passed += 1
print(f"及格人数：{num_passed}")

print("--- 降序成绩 ---")
for index in range(len(sorted_score_list)):
    print(f"第{index+1}位：{sorted_score_list[index]}")