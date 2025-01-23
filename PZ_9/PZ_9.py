# Используя словарь посчитать количество уникальных слов в заданном
# предложении «Изучаем язык Питон». Вывести на экран каждую пару
# «ключ:значение».
sentence = "Изучаем язык пайтон"
word_count = {}
words = sentence.lower().split()
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
for key, value in word_count.items():
    print(f"{key}: {value}")
