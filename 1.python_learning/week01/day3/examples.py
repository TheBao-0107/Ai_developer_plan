bicycleList = ['trek','cannondale','redline','specialized']
print(bicycleList)
print(bicycleList[0])
print(bicycleList[0].title())

friendsNameList = ['Bobby','Eric','James','Aven','crystal','Jessica']
for friendName in friendsNameList:
    print(f"{friendName}, nice to me you!")

TraficMethodList = ['Audi','BMW','Ducati']
print(f"my favourite car brand is {TraficMethodList[0]}")
print(f"I aslo like {TraficMethodList[1]}")
print(f"I would like to own a {TraficMethodList[2]} motocycle")

haveDinnerTogetherNameList = ['KiKi','CoCo','KeKe','代薰月','小白','壮白','灰灰','小虎','阿黄','壮壮','皮球','来福','旺财','小猫','三毛子','大白']

print(f"I have {len(haveDinnerTogetherNameList)-3} Baby")
for name in haveDinnerTogetherNameList:
    print(f'{name}, I really want to have dinner with you')

print('--------------------------------------------------')
print(f"the name who I can not invite together night is 'CoCo'")

changeIndex = haveDinnerTogetherNameList.index('CoCo')
haveDinnerTogetherNameList.remove('CoCo')
haveDinnerTogetherNameList.insert(changeIndex,'Bob')

for name in haveDinnerTogetherNameList:
    print(f'{name}, I really want to have dinner with you')

print('--------------------------------------------------')

print('I have found a bigger Table!')

haveDinnerTogetherNameList.insert(0,'Jason')
haveDinnerTogetherNameList.insert(len(haveDinnerTogetherNameList)//2 + 1,'MoMo')
haveDinnerTogetherNameList.append('Mark')

for name in haveDinnerTogetherNameList:
    print(f'{name}, I really want to have dinner with you')

print('--------------------------------------------------')

theMTFsName = ['YHN','GZL','SSM','JY','WJQ']
print('sorry I can just kill two in you mother fuckers')

while(len(theMTFsName) > 2):
    print(f'FUCK YOU, {theMTFsName.pop()}!')

for MTF in theMTFsName:
    print(f'food time you {MTF} bitch')

delTime = len(theMTFsName)
while(delTime != 0):
    del theMTFsName[0]
    delTime -= 1
print(theMTFsName)
print('--------------------------------------------------')

TravelPlaceList = ['Japan','America','IceLand','Switzerland','Gemerny','xinJiang']
print(TravelPlaceList)
print(sorted(TravelPlaceList))
print(TravelPlaceList)
print(sorted(TravelPlaceList,reverse=True))
print(TravelPlaceList)
TravelPlaceList.reverse()
print(TravelPlaceList)
TravelPlaceList.reverse()
print(TravelPlaceList)
TravelPlaceList.sort()
print(TravelPlaceList)
TravelPlaceList.sort(reverse=True)
print(TravelPlaceList)

#[]访问列表元素
#.append()方法，在末尾添加元素
#.insert(index,x)方法，在index下标处插入元素x，必须传入下标index和值x
#del list[index]语句，在list中删除index下标处的元素，这个要注意一下写法，没有括号，是个“语句”，语句的概念可以研究一下
#.pop()方法，删除列表最后一个元素，返回值是被删除的值
#.remove(x)方法，删除列表中第一个元素x
#.sort(reverse)方法，快排。reverse = True的时候逆序
#sorted(list,reverse)函数，快排list，reverse = True的时候逆序
#.reverse()方法,倒转列表，没有返回值
#len(list)函数，取列表list的长度