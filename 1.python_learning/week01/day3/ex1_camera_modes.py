# 练习 1：相机待测模式。
# 按 task.md 的顺序调整模式列表，输出最终列表、被移出的模式、末项和数量。
# 在下面写你的代码
modeList = ['preview','video','night']
modeList[1] = 'photo'
modeList.append('slow_motion')
delMode = modeList.pop()
print(f"待测模式：{modeList}")
print(f"已移出：{delMode}")
print(f"当前末项：{modeList[-1]}")
print(f"待测模式数：{len(modeList)}")