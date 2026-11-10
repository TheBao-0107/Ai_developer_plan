# W2D1 挑战：拍摄前检查（可选）
# 按 task.md 的数据和优先级检查拍摄条件，只输出一行检查结果。
# 在下面写你的代码
request_mode = "photo"
available_mode_list = ["preview", "photo"]
energy_left = 20
room_left = 500
if request_mode not in available_mode_list:
    print("不支持该模式")
elif energy_left < 20 or room_left < 500:
    print("资源不足")
else:
    print("可以拍摄")
