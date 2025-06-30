import tkinter as tk
from tkinter import ttk

def create_form():
    # Создание главного окна
    root = tk.Tk()
    root.title("User Login and Personal Information")

    # Настройка стиля
    style = ttk.Style()
    style.configure("TFrame", padding=10)
    style.configure("TLabel", padding=5)
    style.configure("TEntry", padding=5)
    style.configure("TRadiobutton", padding=5)
    style.configure("TButton", padding=5)

    # Создание фрейма для информации входа пользователя
    login_frame = ttk.LabelFrame(root, text="User login info")
    login_frame.pack(fill="x", padx=10, pady=10)

    # Поля для информации входа пользователя
    ttk.Label(login_frame, text="Username:").grid(row=0, column=0, sticky="w")
    ttk.Entry(login_frame).grid(row=0, column=1, sticky="ew")

    ttk.Label(login_frame, text="Email:").grid(row=1, column=0, sticky="w")
    ttk.Entry(login_frame).grid(row=1, column=1, sticky="ew")

    ttk.Label(login_frame, text="Password:").grid(row=2, column=0, sticky="w")
    ttk.Entry(login_frame, show="*").grid(row=2, column=1, sticky="ew")

    # Создание фрейма для личной информации
    personal_info_frame = ttk.LabelFrame(root, text="Data diri")
    personal_info_frame.pack(fill="x", padx=10, pady=10)

    # Поля для личной информации
    ttk.Label(personal_info_frame, text="Alamat:").grid(row=0, column=0, sticky="w")
    ttk.Entry(personal_info_frame).grid(row=0, column=1, sticky="ew")

    ttk.Label(personal_info_frame, text="Tanggal lahir:").grid(row=1, column=0, sticky="w")
    ttk.Entry(personal_info_frame).grid(row=1, column=1, sticky="ew")

    ttk.Label(personal_info_frame, text="Usia:").grid(row=2, column=0, sticky="w")
    ttk.Entry(personal_info_frame).grid(row=2, column=1, sticky="ew")

    ttk.Label(personal_info_frame, text="Jenis kelamin:").grid(row=3, column=0, sticky="w")
    gender_frame = ttk.Frame(personal_info_frame)
    gender_frame.grid(row=3, column=1, sticky="w")
    ttk.Radiobutton(gender_frame, text="Pria", value="Pria").pack(side="left")
    ttk.Radiobutton(gender_frame, text="Wanita", value="Wanita").pack(side="left")

    # Чекбокс и кнопки
    ttk.Checkbutton(root, text="Saya bersedia mengikuti aturan forum").pack(anchor="w", padx=10, pady=5)

    button_frame = ttk.Frame(root)
    button_frame.pack(fill="x", padx=10, pady=10)
    ttk.Button(button_frame, text="Reset").pack(side="left", padx=5)
    ttk.Button(button_frame, text="Submit").pack(side="right", padx=5)

    # Запуск главного цикла
    root.mainloop()

create_form()