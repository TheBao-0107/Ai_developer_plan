example_list = ["car_brand","food_brand","clothes_brand"]
for kind_name in example_list:
    print(f"{kind_name.removesuffix("_brand")}")
x,y,z = 0,0,0

CONST_NUM = 1

for i in range(len(example_list)):
    example_list[i] = example_list[i].removesuffix("_brand")
print(example_list)
print(example_list[-1])
print(example_list[:])
print(example_list[0:])
print(example_list[1:])
print(example_list[:2])
print(example_list[:1])
print(example_list[-2:])

example_list.append("computer")
# example_list.insert(1,"computer")
# del example_list[1]
# example_list.remove("computer")
# example_list.pop()
print(example_list)

sorted_copy_list = sorted(example_list)
print(sorted_copy_list)
print(example_list)

#本周总结练习
tag_list = [" INFO ", " Error ", " debug "]
new_tag_list = tag_list[:]
for index in range(len(new_tag_list)):
    new_tag_list[index] = new_tag_list[index].strip()
    new_tag_list[index] = new_tag_list[index].lower()
print(f"原始标签：{tag_list}")
print("规范标签：")
for tag in new_tag_list:
    print(tag)
