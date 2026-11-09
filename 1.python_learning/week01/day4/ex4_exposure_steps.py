# W1D4 可选挑战：曝光参数预览，完整要求见 task.md。
# 从 4、8、12 毫秒的基础曝光生成每档增加 2 毫秒的预览列表，再取出最后两档。
# 在下面写你的代码
exposureDemensions = (4, 8, 12)
listFormat = [value + 2 for value in exposureDemensions]
lastTwo = listFormat[-2:]
print(f"基础曝光：{exposureDemensions}")
print(f"预览曝光：{listFormat}")
print(f"最后两档：{lastTwo}")
