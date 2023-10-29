# Чтение чисел из файла
with open('input.txt', 'r') as file:
    numbers = [int(line) for line in file.readlines()]

# Сортировка чисел по возрастанию
numbers.sort()

# Запись отсортированных чисел в файл
with open('sorted_output.txt', 'w') as file:
    for num in numbers:
        file.write(str(num) + '\n')
