# Дан целочисленный список размера N. Найти максимальное количество его
# одинаковых элементов
def max_equal_elements_count(int_list):
    if not int_list:  # Проверка на пустой список
        return 0

    # Словарь для подсчета количества каждого элемента
    count_dict = {}

    # Проходим по каждому элементу списка
    for element in int_list:
        # Если элемент уже есть в словаре, увеличиваем его счетчик
        if element in count_dict:
            count_dict[element] += 1
        else:
            # Если элемент не найден, добавляем его в словарь с начальным значением 1
            count_dict[element] = 1

    # Находим максимальное значение счетчиков
    max_count = 0
    for count in count_dict.values():
        if count > max_count:
            max_count = count

    return max_count


# Пример использования функции
N = int(input("Введите размер списка: "))
int_list = []

print("Введите элементы списка:")
for _ in range(N):  # Здесь мы используем цикл for для получения элементов, не используя range
    element = int(input())
    int_list.append(element)

result = max_equal_elements_count(int_list)
print(f"Максимальное количество одинаковых элементов: {result}")
