# 练习 1：更新相机配置。按 task.md 完成字典的访问、增删改及缺失配置查询，输出指定的 6 行报告。
# 在下面写你的代码
camera_setting_dict = {"mode":"photo","fps":30,"debug":True}
print(f"初始帧率：{camera_setting_dict["fps"]}")
camera_setting_dict['fps'] = 60
camera_setting_dict['resolution'] = "1920x1080"
del camera_setting_dict["debug"]
print(f"模式：{camera_setting_dict['mode']}")
print(f"更新帧率：{camera_setting_dict['fps']}")
print(f"分辨率：{camera_setting_dict['resolution']}")
print(f"存储路径：{camera_setting_dict.get('storage','未配置')}")
print(f"配置项数：{len(camera_setting_dict)}")