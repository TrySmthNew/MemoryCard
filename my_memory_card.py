from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import

class MemoryCardApp:
    def __init__(self,master):
        self.master = master
        master.title("Memory Card")

self.label = Label(master, text="Нажмите на карту, чтобы узнать ее значение")
self.label.pack()

self.button = Button(master, text="Ответить", command=self.start_test)
self.button.pack()

self.answered = False 

def show_result(self):
    self.label.confirg(text="Значение карты: 10")

self.answer_form = Label(self.master, text="Правильный ответ: 10")
self.answer_form/pack()

self.button.confirg(text="Следующий вопрос")

def show_question(self):
    self.label.confirg(text="Нажмите на карту, чтобы узнать ее значение")

self.answer_form.pack_forget()

self.button.confirg(text="Ответить")

self.answered = False

def start_test(self):
    if self.button.cget("text") == "Ответить":
        self.show_result()
        elif self.button.cget("text") == "Следующий вопрос":
            self.show_question()

if __name__ == '__main__':
    root = Tk()
    app = MemoryCardApp(root)
    root.mainloop()
