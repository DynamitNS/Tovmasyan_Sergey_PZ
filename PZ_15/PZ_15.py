# Приложение НОТАРИАЛЬНАЯ КОНТОРА для некоторой организации. БД
# должна содержать таблицу Нотариальные услуги со следующей структурой записи: ФИО
# клиента, услуга, сумма сделки, комиссионные (доход конторы).
import sqlite3
from tkinter import *


def add_record():
    conn = sqlite3.connect('notary_office.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO Нотариальные_услуги (фио_клиента, услуга, сумма_сделки, комиссионные)
    VALUES (?, ?, ?, ?)
    ''', (fio.get(), service.get(), amount.get(), commission.get()))

    conn.commit()
    conn.close()
    status_label.config(text="Запись добавлена!")


# Создаем GUI
root = Tk()
root.title("Нотариальная контора")

Label(root, text="ФИО клиента:").pack()
fio = Entry(root)
fio.pack()

Label(root, text="Услуга:").pack()
service = Entry(root)
service.pack()

Label(root, text="Сумма сделки:").pack()
amount = Entry(root)
amount.pack()

Label(root, text="Комиссионные:").pack()
commission = Entry(root)
commission.pack()

Button(root, text="Добавить запись", command=add_record).pack()
status_label = Label(root, text="")
status_label.pack()

root.mainloop()