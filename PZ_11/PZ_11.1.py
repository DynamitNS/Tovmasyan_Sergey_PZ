# Шаг 1: Создание исходного файла с числами
numbers = [10, -5, 3, 8, -2, 6, 9, -12, 15, 7, 0, 4, -1]

with open('input_numbers.txt', 'w', encoding='utf-8') as file:
    for number in numbers:
        file.write(f"{number}\n")

# Шаг 2: Чтение данных из файла, обработка и запись результатов
with open('input_numbers.txt', 'r', encoding='utf-8') as file:
    numbers = [int(line.strip()) for line in file if line.strip()]

# Вычисления
count = len(numbers)
min_num = min(numbers)
multiples_of_three = [num for num in numbers if num % 3 == 0]
count_multiples = len(multiples_of_three)

# Запись результатов в новый файл
with open('output_results.txt', 'w', encoding='utf-8') as file:
    file.write("Исходные данные:\n")
    file.write(" ".join(map(str, numbers)) + "\n")
    file.write(f"Количество элементов: {count}\n")
    file.write(f"Минимальный элемент: {min_num}\n")
    file.write(f"Числа кратные трем: {' '.join(map(str, multiples_of_three))}\n")
    file.write(f"Количество чисел кратных трем: {count_multiples}\n")

print("Файлы успешно созданы и обработаны.")