# my_empty_list = []
# my_empty_list_2 = list()
# my_list = [1, 5.6, "Привіт світ", True, False, None, [2,4,6]]
# numbers = [2,8,9,10 -8]
# words = ["word_1", "word_2"]
# print(numbers[1])
# for number in numbers:
#     print(number)
# students = [["Alex", "Kondr", 45], ["Іван", "Іванов", 78]]
# # print(students[0][45])
# for student in students:
# #     print(student[0])
# numbers = [2,8,9,10,-8]
# number = numbers.pop(3)

# print(f"студент № {number} завершив навчання")
# print(f"новий список студентів: {numbers}")
# Створіть програму, яка приймає список товарів та повертає список,
# в якому кожен елемент дорівнює кількості букв, з яких складається товар.


# numbers_letter_for_products = []
# products = ["Сіль", "Хліб", "Цукор", "Паштет"]
# for product in products:
#     count_letter = len(product)
#     numbers_letter_for_products.append(count_letter)

# print(numbers_letter_for_products)

# numbers = []
# if not numbers:
#     numbers.append(5)

# print(numbers)

# numbers_1 = [5,1,-8,1]
# numbers_2 = [0,6]
# numbers_3 = numbers_1 + numbers_2
# numbers_3 = numbers_2 + numbers_1
# print(numbers_3)

# numbers_1 += [45]
# print(numbers_1)

# numbers_1 = [5,1,-8,1,11,78,-64]


# # Написати програму, яка видалить зі списку 1-й, 3-й і 6-й елементи
# numbers_1 = [5, 1, -8, 1, 11, 78, -64]

# my_list = [1, 2, 3, 5]
# print(my_list)
# my_list.append(10)
# print(my_list)

# my_string = "lower text"
# print(my_string)
# my_string_1 = my_string.upper()
# print(my_string_1)




# a = 10

# c = a
# c += 1
# print(c)
# print(a)
# my_list = [1,2,3]
# my_list_copy = my_list.copy()
# print("до..")
# print(f"{my_list_copy = }")
# print(f"{my_list = }")

# my_list_copy.append(10)

# print("після")
# print(f"{my_list_copy = }")
# print(f"{my_list = }")


# my_list = [1, 2, 3]

# element = my_list.pop(0)
# my_list.pop()
# my_list.pop()
# if my_list:
#     my_list.pop()
# # del my_list[0]
# my_list.remove(2)
# print(my_list)

# new_list = [4,5,6,7,8]
# new_list.clearnew_list = []
# print(new_list)
# index = my_list.index(2)
# print(index)

# my_list = [1,2,4,5,5,6,1]
# # count = my_list.count(5)
# # print(count)
# my_list.sort()
# print(my_list)

# my_list.sort(reverse=True)
# # sorted_list = sorted(my_list, reverse = True)
# # print(sorted_list)
# my_list.reverse()
# my_list = my_list[::-1]
# print (my_list)



# count_el = len(my_list)
# print(my_list)
# print(count_el)
# for el in my_list:
#     print(el)

# my_list = [1,2,1,6,5,5,3,1,2,5,6,1]
# if 5 in my_list:
#     print("10 міститьсяу списку ")
# else:


# from pprint import pprint


# products = [
#     "Гречка",
#     "Макарони",
#     "Спагеті",
#     "Картопля",
#     "Буряк",
#     "Морква",
#     "Капуста",
#     "Цибуля",
#     "Часник",
#     "Борошно",
#     "Яйця",
#     "Соняшникова олія",
#     "Вершкове масло",
#     "Сіль",
#     "Перець",
#     "Цукор",
#     "Оцет",
#     "Сода",
#     "Чай",
#     "Кава"
# ]

# products_sold = []

# commands = [
#     "1. Показати список наявних товарів",
#     "2. Додати новий товар до списку",
#     "3. Додати список товарів",
#     "4. Видалити товар за ім'ям",
#     "5. Видалити товар за номер",
#     "6. Показати відсортований список товарів за ім'ям",
#     "7. Продати товар",
#     "8. Знайти номер товару за ім'ям",
#     "9. Показати список проданих товарів",
#     "10. Показати історію продажів",
#     "11. Вийти з програми"
# ]


# while True:
#     comm = input(f"Виберіть дію або введіть exit для завершення:\n{commands}")
#     if comm.lower() == "exit":
#         print("дякуємо")
#         break

#     if int(comm) <= 0 or int(comm) > len(commands):
#         print("Ви ввели не вірну дію, спробуйте ще раз")
#         continue

#     if int(comm) == 1:
#         pprint(products)



