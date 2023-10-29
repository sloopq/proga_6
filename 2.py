# Чтение чисел из файла и разделение строки по пробелу
with open('input.txt', 'r') as file:
    line = file.read()
numbers = [int(num) for num in line.split()]

# Сортировка чисел по возрастанию
numbers.sort()

# Запись отсортированных чисел в файл
with open('sorted_output.txt', 'w') as file:
    for num in numbers:
        file.write(str(num) + '\n')
