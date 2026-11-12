

x = int(input("Введіть координату X:"))
y = int(input("Введіть координату Y:"))



if y > 0:
    if x > 0:
        print("I чверть")
    elif x < 0:
        print("II чверть")
    else:
        print("Точка лежить на осі Y")
elif y < 0:
    if x < 0:
        print("III чверть")
    elif x > 0:
        print("IV чверть")
    else:
        print("Точка лежить на осі Y")
else:
    print("Точка лежить на осі X")