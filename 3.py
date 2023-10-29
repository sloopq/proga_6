# Чтение информации о детях из файла
with open('children.txt', 'r') as file:
    lines = file.readlines()

# Инициализация переменных для поиска самого младшего и самого старшего
youngest_age = float('inf')
oldest_age = 0
youngest_child = ""
oldest_child = ""

# Поиск самого младшего и самого старшего
for line in lines:
    parts = line.split()
    age = int(parts[2])
    if age < youngest_age:
        youngest_age = age
        youngest_child = line
    if age > oldest_age:
        oldest_age = age
        oldest_child = line

# Запись информации о самом младшем и самом старшем ребенке
with open('youngest_child.txt', 'w') as file:
    file.write(youngest_child)

with open('oldest_child.txt', 'w') as file:
    file.write(oldest_child)
