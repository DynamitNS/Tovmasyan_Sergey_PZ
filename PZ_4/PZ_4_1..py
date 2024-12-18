# Дано вещественное число X и целое число N (> 0). Найти значение выражения
# 1 - X2/(2!) + X4/(4!) - ... + (-1)N-X
# 2*N/((2-N)!) (N! = 12 ...N). Полученное число является
# приближенным значением функции cos в точке X.
# Ввод значений X и N
X = float(input("Введите вещественное число X: "))
N = int(input("Введите целое число N (> 0): "))

# Инициализация переменных
result = 1.0  # Начальное значение выражения (первый член)
sign = -1.0   # Знак для следующего члена
current_power = X * X  # Начальное значение X^2
factorial = 2  # Начальное значение для 2!

i = 1  # Индекс для итерации

# Цикл для вычисления суммы
while i <= N:
    result += sign * (current_power / factorial)  # Добавляем текущий член
    sign *= -1.0  # Меняем знак
    current_power *= X * X  # Увеличиваем степень X
    factorial *= (2 * i) * (2 * i - 1)  # Вычисляем факториал (2*i)!
    i += 1  # Увеличиваем индекс

# Вывод результата
print("Приближенное значение cos(X):", result)
