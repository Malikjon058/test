from tkinter import *
from datetime import datetime
from tkinter import messagebox

from data import MyDB

db = MyDB()
db.create_tables()


class Window:
    def __init__(self, title, width=400, height=300, resizeable=(False, False)):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(resizeable[0], resizeable[1])

        self.full_name = StringVar()
        self.username = StringVar()
        self.email = StringVar()
        self.password = StringVar()

        self.label = Label(self.root, text="Регистрация", width=45, font=(15,))

        self.f_label1 = Label(self.root, text="Ф.И.О")
        self.f_entry1 = Entry(self.root, width=30, textvariable=self.full_name)

        self.f_label2 = Label(self.root, text="Логин")
        self.f_entry2 = Entry(self.root, width=30, textvariable=self.username)

        self.f_label3 = Label(self.root, text="Email")
        self.f_entry3 = Entry(self.root, width=30, textvariable=self.email)

        self.f_label4 = Label(self.root, text="Пароль")
        self.f_entry4 = Entry(self.root, width=30, show="#", textvariable=self.password)

        self.submit = Button(self.root, fg="#fff", bg="#1055f6", text="Отправить", height=2, width=10,
                             command=self.reg_btn)

    def draw_widgets(self):
        self.label.grid()

        self.f_label1.grid()
        self.f_entry1.grid()

        self.f_label2.grid()
        self.f_entry2.grid()

        self.f_label3.grid()
        self.f_entry3.grid()

        self.f_label4.grid()
        self.f_entry4.grid()

        self.submit.grid()

    def reg_btn(self):
        now_date = datetime.now().strftime("%Y/%M/%d %H:%m")
        title, message = self.validated_method(email=self.email.get(), password=self.password.get())
        if type(title) is bool:
            db.insert_method(
                full_name=self.full_name.get(),
                username=self.username.get(),
                password=self.password.get(),
                email=self.email.get(),
                date=now_date,
            )

            messagebox.showinfo(title="Поздравляю", message="Вы прошли регистрацию!")
            for i in range(1, 5):
                eval(f"self.f_entry{i}.delete(0, END)")
        else:
            messagebox.showerror(title=title, message=message)

    def validated_method(self, **kwargs):
        if not kwargs['email'].endswith("@mail.ru") and len(kwargs['password']) < 8:
            return "Error", "Ваш email или пароль неправельны"

        if len(kwargs['password']) < 8:
            return "Error Password", "Пароль должен содержать не менее 8 символов!"

        elif not kwargs['email'].endswith("@mail.ru"):
            return "Error Email", "Ваш email неправельны"

        return True, True

    def run(self):
        self.draw_widgets()
        self.root.mainloop()


app = Window('Регистрация!')
app.run()
