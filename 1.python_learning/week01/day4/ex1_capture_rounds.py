# W1D4 练习 1：四轮采集与耗时汇总，完整要求见 task.md。
# 输出第 1 至第 4 轮采集提示，并统计 36、28、40、24 毫秒中的最短、最长和总耗时。
# 在下面写你的代码
for round in range(1, 5):
    print(f"第 {round} 轮采集")
timeCosts = [36, 28, 40, 24]
unit = "ms"
print(f"最短耗时：{min(timeCosts)} {unit}")
print(f"最长耗时：{max(timeCosts)} {unit}")
print(f"总耗时：{sum(timeCosts)} {unit}")
