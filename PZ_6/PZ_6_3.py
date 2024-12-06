# Дан список размера N, все элементы которого, кроме одного, упорядочены по
# убыванию. Сделать список упорядоченным, переместив элемент, нарушающий
# упорядоченность, на новую позицию.
def find_and_correct_disorder(int_list):
    N = len(int_list)

    # Найдем индекс элемента, нарушающего порядок
    disorder_index = -1
    for i in range(1, N):
        if int_list[i] > int_list[i - 1]:
            disorder_index = i
            break

    # Если порядок не нарушен, возвращаем оригинальный список
    if disorder_index == -1:
        return int_list

    # Элемент, нарушающий порядок
    disorder_element = int_list[disorder_index]

    # Удаляем элемент из списка
    int_list.pop(disorder_index)

    # Найдем правильное место для disorder_element
    insert_index = 0
    while insert_index < len(int_list) and int_list[insert_index] >= disorder_element:
        insert_index += 1

    # Вставляем элемент на правильную позицию
    int_list.insert(insert_index, disorder_element)

    return int_list


# Пример использования функции
N = int(input("Введите размер списка: "))
int_list = []

print("Введите элементы списка:")
for _ in range(N):  # Используем цикл for для ввода элементов
    element = int(input())
    int_list.append(element)

sorted_list = find_and_correct_disorder(int_list)
print("Упорядоченный список:", sorted_list)
