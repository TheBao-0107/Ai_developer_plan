# W2D1 练习 2：清理并判断日志标签（基础）
# 按 task.md 的要求保留原始列表，在副本中清理标签，再判断是否需要处理。
# 在下面写你的代码
log_list = [" ERROR ", "Info", " warning ", "debug"]
copy_log_list = log_list[:]
for index in range(len(copy_log_list)):
   copy_log_list[index] = copy_log_list[index].strip().lower()
print(f"原始：{log_list}")
print(f"清理后：{copy_log_list}")

need_process_log_list = ["error","warning"]
for log in copy_log_list:
    print(log,end="")
    if log in need_process_log_list:
      print("：需要处理")
    else:
      print("：无需处理")
