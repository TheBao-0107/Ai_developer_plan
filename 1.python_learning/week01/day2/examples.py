#2026/11/03/21：53
#Just a Test for Day2
printMsg = "Boring"
print(printMsg)

printMsg = "Good"
print(printMsg)

name = "alibaba company!"
fullName = name.title()
print(fullName)

allBigWord = name.upper()
print(allBigWord)
print(f"{allBigWord}")

allSmallWord = name.lower()
print(f"{allSmallWord}")

fansSaidThat = f"I Like {name.title()}"
print(f"{fansSaidThat}")

print(f"{fansSaidThat}\n换行{fansSaidThat}")

print(f"\t{fansSaidThat}\n\t换行缩进{fansSaidThat}")

testStr1 = "\t"
testStr2 = "    "
print(f"\tStr1 ={testStr1},Str2 ={testStr2},Thats all")

testStr3 = "  Hello  "
print(f"the String={testStr3.rstrip()},the len is {len(testStr3.rstrip())}")
print(f"the String={testStr3.strip()},the len is {len(testStr3.strip())}")
print(f"the String={testStr3.lstrip()},the len is {len(testStr3.lstrip())}")

testJson = ["Player张三","Player李四","Player王五"]
for testStr in testJson:
    print(f"{testStr.removeprefix("Player")}",end=" ")
print("")

testName = "Eric"
print(f"Hi {testName},would you like to have dinner with me?")
nameUpper = testName.upper()
nameLower = testName.lower()
nameTitle = testName.title()
print(f"upperStr={nameUpper},lowerStr={nameLower},titleStr={nameTitle}")

famousName = "SpiderMan"
famousTalk = "能力越大,责任越大"
print(f'{famousName} once said that "{famousTalk}"')

message = f'{famousName} once said that "{famousTalk}"'
print(message)

wrongName = "\tPeter\n   "
print(wrongName)
print(f"{wrongName.strip()},lets go")
print(f"{wrongName.rstrip()},lets go")
print(f"{wrongName.lstrip()},lets go")

testJson1 = ["ChatGPT.exe","Claude.exe","Gemini.exe"]
for testJson in testJson1:
    print(f'{testJson.removesuffix(".exe")}',end=" ")
print("")
print(1+7)
print(9-1)
print(2 ** 3)
print(1*8)
print(8/1)

favouriteNum = (17-10)
printMessage = f"my favourite num is '{favouriteNum}'"
print(f"{printMessage}")

##注释Test
#注释