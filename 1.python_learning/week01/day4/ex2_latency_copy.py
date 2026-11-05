# W1D4 练习 2：保留原始顺序的耗时报告，完整要求见 task.md。
# 从 42、18、35、27 毫秒的记录生成排序副本和最快两次，保留原始记录顺序。
# 在下面写你的代码
timeCostList = [42, 18, 35, 27]
copyList = timeCostList[:]
copyList.sort()
sliceCopyList = copyList[:2]
print(f"原始耗时：{timeCostList}")
print(f"排序副本：{copyList}")
print(f"最快两次：{sliceCopyList}")
