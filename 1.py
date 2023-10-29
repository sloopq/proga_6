# Чтение чисел из файла
with open('input.txt', 'r') as file:
    numbers = file.read().split()

# Преобразование строк в числа
numbers = [int(num) for num in numbers]

# Вычисление произведения
product = 1
for num in numbers:
    product *= num

# Запись произведения в файл
with open('output.txt', 'w') as file:
    file.write(str(product))
