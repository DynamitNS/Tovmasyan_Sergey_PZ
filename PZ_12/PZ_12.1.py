# В последовательности на n целых элементов в первой ее половине найти
# количество положительных элементов.
n = int(input("Введите количество элементов последовательности: "))
sequence = list(map(int, input("Введите последовательность целых чисел через пробел: ").split()))

half = n // 2
first_half = sequence[:half]
count_positive = sum(1 for num in first_half if num > 0)

print("Количество положительных элементов в первой половине:", count_positive)