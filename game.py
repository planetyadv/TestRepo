import tkinter as tk
from tkinter import messagebox

# Функция для тестирования бинарного кода
def test_binary_code(binary_code):
    try:
        # Преобразуем бинарный код в строку
        binary_string = ''.join(chr(int(binary_code[i:i+8], 2)) for i in range(0, len(binary_code), 8))
        return binary_string
    except ValueError:
        return "Ошибка! Неверный бинарный код."

# Функция для открытия тестераd
def open_tester():
    tester_window = tk.Toplevel(root)
    tester_window.title("Binary Code Tester")
    
    # Ввод бинарного кода
    test_label = tk.Label(tester_window, text="Введите бинарный код:")
    test_label.pack(pady=5)
    
    # Многострочное поле ввода
    binary_input = tk.Text(tester_window, height=10, width=50)
    binary_input.pack(pady=5)
    
    # Кнопка для тестирования
    def on_test():
        binary_code = binary_input.get("1.0", "end-1c").replace("\n", "")  # Получаем весь текст без завершающих символов
        result = test_binary_code(binary_code)
        result_label.config(text=f"Результат: {result}")

    test_button = tk.Button(tester_window, text="Тестировать", command=on_test)
    test_button.pack(pady=10)
    
    # Кнопка для вставки текста из буфера обмена
    def on_paste():
        clipboard_content = root.clipboard_get()  # Получаем текст из буфера обмена
        binary_input.insert("1.0", clipboard_content)  # Вставляем в поле ввода

    paste_button = tk.Button(tester_window, text="Вставить текст", command=on_paste)
    paste_button.pack(pady=10)
    
    # Результат тестирования
    result_label = tk.Label(tester_window, text="Результат:")
    result_label.pack(pady=5)

# Функция для отображения подсказки
def show_tooltip(event, text):
    tooltip = tk.Toplevel(root)
    tooltip.wm_overrideredirect(True)
    tooltip.geometry(f"+{event.x_root + 10}+{event.y_root + 10}")
    tooltip_label = tk.Label(tooltip, text=text, background="yellow", relief="solid", padx=5, pady=5)
    tooltip_label.pack()
    
    # Закрытие подсказки при уходе курсора
    def hide_tooltip(event):
        tooltip.destroy()
    
    tooltip_label.bind("<Leave>", hide_tooltip)

# Основное окно программы
root = tk.Tk()
root.title("BinarySalad")

# Ввод бинарного кода
label = tk.Label(root, text="Введите бинарный код:")
label.pack(pady=5)

# Многострочное поле ввода
binary_input = tk.Text(root, height=10, width=50)
binary_input.pack(pady=5)

# Добавление подсказки для поля ввода
binary_input.bind("<Enter>", lambda event: show_tooltip(event, "Введите бинарный код (например: 01001000 01100101 01101100 01101100 01101111)"))

# Кнопка для отправки кода в тестер
open_button = tk.Button(root, text="Открыть тестер", command=open_tester)
open_button.pack(pady=20)

# Добавление подсказки для кнопки
open_button.bind("<Enter>", lambda event: show_tooltip(event, "Открыть окно тестера для проверки бинарного кода"))

# Основной цикл
root.mainloop()
