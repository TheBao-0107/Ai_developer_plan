def display_message(message):
    """打印消息"""
    print(f"本章的主题是：{message}")


display_message("函数")


def favorite_book(title):
    """打印最喜欢的书"""
    print(f"One of my favorite book is {title}")


favorite_book("Alice in Wonderland")


def make_shirt(text="I love Python"):
    """制作有对应文字印花的T恤"""
    print(f"{text}")


make_shirt()
make_shirt(text="I love JAVA")
make_shirt()
make_shirt("I love C++")


def describe_city(city="Shanghai", country="China"):
    """展示城市和国家的关系"""
    print(f"{city} is in {country}")


describe_city("shanghai")
describe_city(city="Boston", country="The USA")
describe_city("London", "The UK")


def city_country(city, country):
    """返回城市和国家组成的字符串"""
    return f"{city}, {country}"


print(city_country("cityA", "countryA"))
print(city_country(city="cityB", country="countryB"))

def make_album(singer,album,number=None):
    """返回歌手和专辑和专辑曲目数信息组成的字典"""
    if number:
        return {'singer':singer,'album':album,'number':number}
    else:
        return {'singer':singer,'album':album}

while True:
    singer = input('请输入歌手名（退出请输入‘q’）：\n')
    if singer=='q':
        break
    album = input('请输入专辑名（退出请输入‘q’）：\n')
    if album=='q':
        break
    print(f"{make_album(singer,album)}")
