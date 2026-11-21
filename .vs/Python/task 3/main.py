# a = 2
# while a < 7:
#     a += 1
#     print(a)

# my_string_1 = "Привіт світ"
# my_string_2 = "інший чфыавыавыав рядок"
# i = 0
# while len(my_string_1) < 40:
#     my_string_1 += my_string_2[i]
#     i += 1


# print(f"{my_string_1 = }")


# while True:
#     my_string_1 = input("Введіть рядок: ")
#     if my_string_1 == "exit":
#         print ("дяукую за використання програми")
#         break
#     print(f"Ви ввели рядок: {my_string_1}")
# print("Програма завершила роботу")



# numbers = [i for i in range(20)]
# print (numbers)


# sum = 0
# count = 0
# for i in range(100):
#     if i % 3 == 0:
#         sum += i
#         count += 1
# avg = sum / count
# print(f"Середнє арифметичне дорівнює: {avg}")




# for i in range(20):
#     print(f"{i = }")
#     for j in range(2):
#         print(f"{j = }")
#         if j > 3:
#             break
#     break

# while True:
    # number = input("Введіть число: ")
    # if not number.isdigit() or int(number) < 1 or int(number) > 1000:
    #     print("Введено число поза межами діапазону. Спробуйте ще раз.")
    #     continue
    # number = int(number)
    # if number < 10:
    #     name = "Одноцифрове"
    # elif number < 100:
    #     name = "Двоцифрове"
    # else:
    #     name = "Трицифрове"
    
    # is_odd = True if number % 2 != 0 else False
    # print(f"Число {"парне" if not is_odd else 'непарне'} {name.lower()}")


a = int(input("Введіть початок діапазону: "))
b = int(input("Введіть кінець діапазону: "))
multiple = 1 
for i in range(a, b + 1):
    multiple *= i
print(f"добуток чисел від {a} до {b}: {multiple}")

