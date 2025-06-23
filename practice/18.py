# 18. Рисуем линии, прямоугольники, круг и текст в Tkinter 

import tkinter as tk


window = tk.Tk()
window.title("Tkinter Графика")


canvas = tk.Canvas(window, width=500, height=400, bg="white")
canvas.pack()


canvas.create_line(50, 50, 450, 50, fill="blue", width=3, dash=(4, 4))


canvas.create_rectangle(50, 80, 250, 180, fill="green",
                        outline="black", width=2)


canvas.create_oval(300, 80, 450, 230, fill="yellow", outline="orange", width=4)


canvas.create_text(
    250, 280,
    text="Это графические примитивы\nв Tkinter",
    font=("Courier", 16, "italic"),
    fill="purple",
    justify=tk.CENTER
)


window.mainloop()
