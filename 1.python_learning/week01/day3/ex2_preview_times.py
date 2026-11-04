# 练习 2：预览耗时排序。
# 按 task.md 的要求比较临时排序、永久排序和反转的结果。
# 在下面写你的代码
timeCostList = [36,24,48,30]
print(f"临时升序：{sorted(timeCostList)}")
print(f"原始顺序：{timeCostList}")
timeCostList.sort()
print(f"永久升序：{timeCostList}")
timeCostList.reverse()
print(f"反转之后：{timeCostList}")