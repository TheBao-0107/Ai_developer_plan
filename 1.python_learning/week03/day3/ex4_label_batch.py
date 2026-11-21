# 可选挑战：给导入的标签函数取别名，为同一柜格的工具逐件打标签。
# 在下面写你的代码
from ex1_shelf_label import tag_label as tag

tool_list = ["扳手", "钳子"]
for tool in tool_list:
    print(tag("C3", tool))
