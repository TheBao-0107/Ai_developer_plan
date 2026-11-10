# 练习 2：相机模块超时报告。按 task.md 遍历模块与次数，判断状态并汇总，注意嵌套缩进。
# 在下面写你的代码
timeout_report_dict = {"preview": 2, "capture": 0, "encode": 4}
for key,value in timeout_report_dict.items():
    printStr = "正常"
    if value > 0:
        printStr = "需检查"
    print(f"{key}：{value} 次，{printStr}")
print(f"超时总次数：{sum(timeout_report_dict.values())}")