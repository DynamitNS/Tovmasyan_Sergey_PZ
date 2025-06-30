# Найдите минимальный и максимальный элементы в двумерном списке.
matrix = [
    [5, 3, 8],
    [1, 9, 4],
    [7, 2, 6]
]

flattened = [num for row in matrix for num in row]

min_val = min(flattened)
max_val = max(flattened)

print(f"Минимальный элемент: {min_val}")
print(f"Максимальный элемент: {max_val}")