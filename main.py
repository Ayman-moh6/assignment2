# first
numbers = [12, 75, 150, 180, 145, 525, 50]
for num9 in numbers:
    if num9 > 500:
        break
    elif num9 > 150:
        continue
    elif num9 % 5 == 0:
        print(num9)


    print('-----------------------------------------------------')
# second
    for do in range(5):
     print(do)
    else:
     print("Done!")


    print('-----------------------------------------------------')
# third
    number = 76542
    reversenumber = 0
    while number > 0:
        reminder = number % 10
        reversenumber = (reversenumber * 10) + reminder
        number = number // 10
    print(reversenumber)


    print('-----------------------------------------------------')
# fourth
    de1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    de2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

    de3 = {**de1, **de2}
    print(de3)


    print('-----------------------------------------------------')
    # fifth
    dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }
    keys = ["name", "salary"]

    dict = {dk: dict[dk] for dk in dict.keys() - keys}
    print(dict)
