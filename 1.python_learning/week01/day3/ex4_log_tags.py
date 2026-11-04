# 可选挑战：整理相机日志标签。
# 按 task.md 的顺序插入、删除标签，输出最终列表和数量。
# 在下面写你的代码
logList = ['boot', 'preview', 'capture', 'stop']
logList.insert(logList.index('capture')-1,'focus')
logList.remove('preview')
del logList[0]
print(f"保留标签：{logList}")
print(f"标签数：{len(logList)}")