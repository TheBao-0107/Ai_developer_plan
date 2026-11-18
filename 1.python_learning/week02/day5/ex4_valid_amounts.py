# 可选挑战：跳过无效金额。按 task.md 使用 while 和 continue 统计有效记录，并确保循环正常结束。
# 在下面写你的代码
amounts_list = [5, 0, 8, -2, 3]
valid_list = []
index = 0
while index < len(amounts_list):
    if amounts_list[index] > 0:
        valid_list.append(amounts_list[index])
        index += 1
    else:
        index += 1
        continue
print(f"有效记录：{len(valid_list)}笔")
print(f"合计：{sum(valid_list)}元")
print("处理结束")
