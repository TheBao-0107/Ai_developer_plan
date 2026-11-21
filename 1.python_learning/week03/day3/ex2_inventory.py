# 练习 2：调用工具标签模块，将两件工具分别登记到指定的盘点单。
# 在下面写你的代码
import ex1_shelf_label

first_list = []
second_list = []


def func_inventory(cabinet, tool, target_list):
    """将柜格信息盘点到列表中"""
    target_list.append(ex1_shelf_label.tag_label(cabinet, tool))


func_inventory("A2", "卷尺", first_list)
func_inventory("B1", "手电", second_list)
print(first_list)
print(second_list)
