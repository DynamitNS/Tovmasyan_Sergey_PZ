# Дан список размера N и целые числа K и L (1 < K < L < N ). Найти среднее
# арифметическое элементов список с номерами от K до L включительно.
def average_of_sublist(lst, K, L):
    # Проверяем, что K и L находятся в допустимых пределах
    if K < 1 or L >= len(lst) or K > L:
        raise ValueError("Индексы K и L должны быть в диапазоне от 1 до N и K < L.")

    # Суммируем элементы от K до L включительно
    total_sum = 0
    count = 0

    for i in range(K - 1, L):  # Индексы в Python начинаются с 0, поэтому K-1
        total_sum += lst[i]
        count += 1

    # Вычисляем среднее арифметическое
    average = total_sum / count
    return average


# Пример использования функции
N = 10
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Пример списка
K = int(input("Введите значение "))
L = int(input("Введите значение "))

result = average_of_sublist(my_list, K, L)
print(f"Среднее арифметическое элементов с индексами от {K} до {L}: {result}")
