foodList = ["bread", "burger", "cake", "meat", "milk", "beaf"]
friendFoodList = foodList[:]
friendFoodList.append("vinegar")
for food in foodList:
    print(f"I like eat {food}")
print("I am a fat pig")
for food in friendFoodList:
    print(f"She like eat {food}")

animalList = ["tiger", "cat", "dog"]
for animal in animalList:
    print(f"{animal} have a tail")
print(f"every of these animals have a tail")

print("--------------------------------------------------")

# 生成1-10的平方组成的列表
squares = []
for num in range(1, 11):
    squares.append(num**2)
print(squares)

squares = []
squares = [value**2 for value in range(1, 11)]
print(squares)

for num in range(1, 21):
    print(num)

# numList = range(1,1_000_001)
# for num in numList:
#     print(num)

# print(f"max in list is {max(numList)}")
# print(f"min in list is {min(numList)}")
# sum(numList)

singleNumList = range(1, 21, 2)
for num in singleNumList:
    print(num)

tripleList = []
for num in range(3, 31):
    if num % 3 == 0:
        tripleList.append(num)
print(tripleList)

listTest = []
for num in range(1, 11):
    listTest.append(num**3)
print(f"cubeNumList {listTest}")

cubeList = [value**3 for value in range(1, 11)]
print(cubeList)

print(f"the first three cube num in the list is {cubeList[:3]}")

print("--------------------------------------------------")

foodDemensions = ("cake", "bread", "egg", "water", "juice")
for food in foodDemensions:
    print(f"{food}")
foodDemensions = ("cake", "chocolate", "vegatable", "water", "juice")
for food in foodDemensions:
    print(f"{food}")
