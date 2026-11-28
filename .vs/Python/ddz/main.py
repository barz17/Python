text = input("Введите числа через пробел: ")
parts = text.split()

numbers = []
for item in parts:
    numbers.append(int(item))

for i in range(1, len(numbers), 2):
    print(numbers[i], end=" ")






text = input("Введите числа через пробел: ")
parts = text.split()

numbers = []
for item in parts:
    numbers.append(int(item))

result = []
for num in numbers:
    if num % 2 != 0:
        result.append(num)

print(result)




text = input("Введите слова через пробел: ")
words = text.split()

reversed_words = []
for i in range(len(words) - 1, -1, -1):
    reversed_words.append(words[i])

print(reversed_words)






text = input("Введите числа через пробел: ")
parts = text.split()

numbers = []
for item in parts:
    numbers.append(int(item))

total = 0
for num in numbers:
    total = total + num

average = total / len(numbers)

result = []
for num in numbers:
    if num < average:
        result.append(num)

print("Среднее:", average)
print("Меньше среднего:", result)