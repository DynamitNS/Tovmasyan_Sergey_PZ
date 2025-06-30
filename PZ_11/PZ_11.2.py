# Из предложенного текстового файла (text18-20.txt) вывести на экран его содержимое,
# количество символов в тексте. Сформировать новый файл, в который поместить строку
# наибольшей длины.

with open('text18-20.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print("Содержимое файла:")
    print(content)
    try:
        with open('text18-20.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            print("Содержимое файла:")
            print(content)
    except FileNotFoundError:
        print("Ошибка: файл не найден!")
        exit(1)
