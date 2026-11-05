print("як тебе звати?")
input_name = input()
if input_name == "Артем":
    print("фу бля")
print(f"Привіт, {input_name}.")
print("скільки тобі років?")
input_age = input()
print(f"Тобі {input_age} років.")
next_year_age = int(input_age) + 1
print(f"Наступного року тобі буде {next_year_age} років.")
while input_age < "0" or input_age > "100":
    if input_age >= "0" or input_age <= "100":
        break
    else:
        print("Иди нахуй, напиши реально")
    input_age = input("Введи свій вік (0-100): ")
    if input_age >= "0" and input_age <= "100":
        next_year_age = int(input_age) + 1
        print(f"Наступного року тобі буде {next_year_age} років.")
    break

#if input_age >= "0" and input_age <= "100":
    next_year_age = int(input_age) + 1
    print(f"Наступного року тобі буде {next_year_age} років.")
print("яка твоя улюблена гра?")
input_game = input()
print(f"Твоя улюблена гра: {input_game}.")