# В двумерном списке найдите сумму элементов первых двух строк.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

sum_row1 = sum(matrix[0])

sum_row2 = sum(matrix[1])

total_sum = sum_row1 + sum_row2

print(f"Сумма первой строки: {sum_row1}")
print(f"Сумма второй строки: {sum_row2}")
print(f"Общая сумма первых двух строк: {total_sum}")
