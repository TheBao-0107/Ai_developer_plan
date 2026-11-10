alien_color = "green"
if alien_color == "green":
    print("you killed the alien, got 5 point!")
elif alien_color == "yellow":
    print("you got 10 point!")
elif alien_color == "red":
    print("you got 15 point!")

age = 23
if age < 2:
    print("this person is a baby")
elif age < 4:
    print("this person is a kid")
elif age < 13:
    print("this person is a child")
elif age < 18:
    print("this person is a teenager")
elif age < 65:
    print("this person is an adult")
else:
    print("this person is an elder")

favorite_fruit = ["watermalon", "Kiwi fruit(sliced by Mom)", "peach"]

if favorite_fruit:
    if "bananas" in favorite_fruit:
        print("You really like bananas")
    if "apple" in favorite_fruit:
        print("You really like apples")
else:
    print("Hey, you gonna eat some fruit!")
