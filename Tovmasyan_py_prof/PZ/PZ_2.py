# Дано трехзначное число. Вывести число, полученное при
# перестановке цифр сотен и десятков исходного числа (например, 123 перейдет в 213).
f = int(input('Введите трёхзначное число    '))
a = (f % 10)
b = (f % 100 // 10)
c = (f // 100)
v = b * 100 + c * 10 + a
if 100 <= f <= 999:
    print(v, "Программа завершена успешно")
else:
    print("Надо ввести ТРЁХЗНАЧНОЕ число")
