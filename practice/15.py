# 15. а).Tkinter.Создать форму произвольного размера
# б).На этой форме разместить следующие элементы:
# a)Button
# b)Label
# c)Entry
# в).Каждый элемент имеет свою цветовую характеристику(фон,текст)
# г).Обработать нажатие или выбор для каждого элемента выдав соответствующее сообщение.


import tkinter as tk
from tkinter import messagebox


def on_button_click():
    """Вызывается при нажатии на кнопку."""
    entry_text = entry.get()
    messagebox.showinfo("Нажатие на кнопку",
                        f"Кнопка нажата!\nТекст в поле: '{entry_text}'")


def on_label_click(event):
    """Вызывается при клике на метку."""
    messagebox.showinfo("Клик по метке", "Вы кликнули на текстовую метку!")


def on_entry_return(event):
    """Вызывается при нажатии Enter в поле ввода."""
    messagebox.showinfo("Нажатие Enter", "Вы нажали Enter в поле для ввода.")


window = tk.Tk()
window.title("Экзаменационная форма")
window.geometry("400x300")
window.configure(bg="#e0e0e0")  # Фон для всего окна

label = tk.Label(
    window,
    text="Это текстовая метка (кликни по мне)",
    fg="darkblue",      # Цвет текста (foreground)
    bg="#aaeebb",      # Цвет фона (background)
    font=("Arial", 14, "bold")
)

button = tk.Button(
    window,
    text="Нажми меня!",
    fg="white",         # Цвет текста
    bg="#ff5733",       # Цвет фона
    activebackground="#c70039",  # Цвет фона при нажатии
    command=on_button_click  # г). Обработка нажатия
)

entry = tk.Entry(
    window,
    fg="black",         # Цвет текста
    bg="white",         # Цвет фона
    width=30,
    font=("Verdana", 12)
)

label.pack(pady=20)
button.pack(pady=10)
entry.pack(pady=10)

label.bind("<Button-1>", on_label_click)  # <Button-1> - левая кнопка мыши
entry.bind("<Return>", on_entry_return)  # <Return> - клавиша Enter

window.mainloop()
