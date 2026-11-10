# 可选挑战：日志级别计数。按 task.md 从空字典开始统计日志级别，按名称排序输出次数。
# 在下面写你的代码
log_list = ['info','warn','info','error','warn','info']
log_counts_dict = {}
for log in log_list:
    if log_counts_dict.get(log):
        log_counts_dict[log] += 1
    else:
        log_counts_dict[log] = 1

for log in sorted(log_counts_dict.keys()):
    print(f"{log}：{log_counts_dict[log]}")