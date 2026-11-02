# 练习 1：按照 task.md 的示例输出三行相机采集日志。
# 在下面写你的代码
logTitle = "[CameraHAL]"
strOpen = "OPEN"
strFrame001 = "FRAME 001"
strClose = "CLOSE"
printArray = [strOpen, strFrame001, strClose]
for str in printArray:
    print(f"{logTitle} {str}")
