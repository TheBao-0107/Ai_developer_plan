# 练习 1：读取相机编号，转换为整数，判断奇偶并按 task.md 输出。
# 在下面写你的代码
camera_num = int(input("请输入相机编号（整数）："))
if camera_num % 2 == 0:
    print(f"相机{camera_num}：偶数编号")
else:
    print(f"相机{camera_num}：奇数编号")
