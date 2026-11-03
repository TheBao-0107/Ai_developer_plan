# 练习 2（基础）：采集帧数统计
# 要求、示例输出和验收清单见同目录 task.md。
# 在下面写你的代码
timeNum = 2
SumNum = 23
onceNum = 5
averageNum = SumNum/timeNum
fullNum = SumNum//onceNum #或者写成int(SumNum/onceNum)
leftNum = SumNum%onceNum

print(f"采集帧数：{SumNum}")
print(f"平均帧率：{averageNum} 帧/秒")
print(f"完整批次：{fullNum}")
print(f"剩余帧数：{leftNum}")