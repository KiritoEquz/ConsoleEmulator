import tkinter as tk
from tkinter import scrolledtext

class ConsoleEmulator(tk.Tk):
    """
    Класс для эмулятора командной строки на основе Tkinter.
    """
    def __init__(self):
        super().__init__()
        self.title("Эмулятор Оболочки")
        self.geometry("600x400")
        self.configure(bg="black")

        # Создаем текстовое поле для вывода с прокруткой
        self.output_text = scrolledtext.ScrolledText(self, wrap=tk.WORD, state='disabled', height=20, bg="black", fg="lightgreen", font=("Courier New", 10))
        self.output_text.pack(pady=0, padx=0, fill="both", expand=True)

        # Создаем фрейм для строки ввода и приглашения
        input_frame = tk.Frame(self, bg="black")
        input_frame.configure(background="black")
        input_frame.pack(fill="x", padx=0, pady=(0, 10))


        # Приглашение к вводу
        self.prompt_label = tk.Label(input_frame, text="VFS>", font=("Courier New", 10), bg="black", fg="lightgreen")
        self.prompt_label.pack(side="left")

        # Поле для ввода команд
        self.entry = tk.Entry(input_frame, font=("Courier New", 10), relief="flat", bg="black", fg="lightgreen", insertbackground="white")
        self.entry.pack(side="left", fill="x", expand=True)
        self.entry.focus_set() # Устанавливаем фокус на поле ввода при запуске

        # Привязываем событие нажатия Enter к функции обработки команды
        self.entry.bind("<Return>", self.process_command)

        self.write_output("Прототип эмулятора оболочки запущен.\nВведите 'exit' для выхода.\n")

    def write_output(self, message):
        """
        Выводит сообщение в текстовое поле.
        """
        self.output_text.config(state='normal')
        self.output_text.insert(tk.END, message + "\n")
        self.output_text.config(state='disabled')
        # Автоматическая прокрутка вниз
        self.output_text.see(tk.END)

    def process_command(self, event):
        """
        Обрабатывает введенную пользователем команду.
        """
        user_input = self.entry.get()
        if not user_input:
            return

        # Отображаем введенную команду в выводе
        self.write_output(f"VFS> {user_input}")
        self.entry.delete(0, tk.END)

        # Простой парсер: разделяем команду и аргументы по пробелам
        parts = user_input.split()
        command = parts[0]
        args = parts[1:]

        # Выполнение команд
        if command == "ls":
            self.ls_command(args)
        elif command == "cd":
            self.cd_command(args)
        elif command == "exit":
            self.exit_command()
        else:
            self.write_output(f"Ошибка: неизвестная команда '{command}'")

    def ls_command(self, args):
        """
        Реализация команды-заглушки 'ls'.
        """
        self.write_output(f"Вызвана команда 'ls' с аргументами: {args}")

    def cd_command(self, args):
        """
        Реализация команды-заглушки 'cd'.
        """
        if len(args) != 1:
            self.write_output("Ошибка: команда 'cd' требует ровно один аргумент.")
        else:
            self.write_output(f"Вызвана команда 'cd' с аргументами: {args}")

    def exit_command(self):
        """
        Реализация команды 'exit'.
        """
        self.destroy()

if __name__ == "__main__":
    app = ConsoleEmulator()
    app.mainloop()