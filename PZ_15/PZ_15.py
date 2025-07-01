# Приложение НОТАРИАЛЬНАЯ КОНТОРА для некоторой организации. БД
# должна содержать таблицу Нотариальные услуги со следующей структурой записи: ФИО
# клиента, услуга, сумма сделки, комиссионные (доход конторы).
import sqlite3
from sqlite3 import Error


class NotarialOfficeDB:
    def __init__(self, db_file="notarial_office.db"):
        """Инициализация класса с подключением к БД"""
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file)
            self.create_table()
        except Error as e:
            print(f"Ошибка подключения к базе данных: {e}")

    def create_table(self):
        """Создание таблицы услуг, если она не существует"""
        sql = """CREATE TABLE IF NOT EXISTS notarial_services (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    client_id TEXT NOT NULL,
                    service TEXT NOT NULL,
                    amount REAL NOT NULL,
                    commission REAL NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );"""
        try:
            c = self.conn.cursor()
            c.execute(sql)
        except Error as e:
            print(f"Ошибка создания таблицы: {e}")

    def add_service(self, client_id, service, amount, commission):
        """Добавление новой услуги в БД"""
        sql = """INSERT INTO notarial_services(client_id, service, amount, commission)
                 VALUES(?,?,?,?)"""
        try:
            c = self.conn.cursor()
            c.execute(sql, (client_id, service, amount, commission))
            self.conn.commit()
            print(f"Услуга для клиента {client_id} успешно добавлена")
        except Error as e:
            print(f"Ошибка добавления услуги: {e}")

    def get_all_services(self):
        """Получение всех услуг из БД"""
        try:
            c = self.conn.cursor()
            c.execute("SELECT * FROM notarial_services")
            rows = c.fetchall()
            return rows
        except Error as e:
            print(f"Ошибка получения данных: {e}")
            return []

    def display_services(self):
        """Вывод всех услуг в виде таблицы"""
        services = self.get_all_services()
        if not services:
            print("Нет данных об услугах")
            return

        print("\nНОТАРИАЛЬНАЯ КОНТОРА - ВСЕ УСЛУГИ")
        print("{:<5} {:<15} {:<25} {:<15} {:<15} {:<20}".format(
            'ID', 'ID клиента', 'Услуга', 'Сумма', 'Комиссия', 'Дата создания'))
        print("-" * 95)

        for service in services:
            print("{:<5} {:<15} {:<25} {:<15} {:<15} {:<20}".format(
                service[0], service[1], service[2], service[3], service[4], service[5]))

    def close_connection(self):
        """Закрытие соединения с БД"""
        if self.conn:
            self.conn.close()
            print("Соединение с базой данных закрыто")


# Пример использования
if __name__ == "__main__":
    office = NotarialOfficeDB()

    # Добавление услуг
    office.add_service("12345", "Заверение договора", 5000, 500)
    office.add_service("12346", "Свидетельствование подписи", 2000, 200)
    office.add_service("12347", "Удостоверение доверенности", 3500, 350)

    # Вывод всех услуг
    office.display_services()

    # Закрытие соединения
    office.close_connection()