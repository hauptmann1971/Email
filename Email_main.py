from Email_logic import *
from tkinter import *
from tkinter import messagebox as mb

root = Tk()
root.title("Отправка e-mail")
root.geometry("500x420")

lb_from = Label(root, text="Отправитель", font="Arial 14")
lb_from.grid(row=0, column=0, pady=10)
e_from = Entry(root, width=30, font="Arial 14")
e_from.grid(row=0, column=1, pady=10)

lb_to = Label(root, text="Получатель", font="Arial 14")
lb_to.grid(row=1, column=0, pady=10)
e_to = Entry(root, width=30, font="Arial 14")
e_to.grid(row=1, column=1, pady=10)

lb_password = Label(root, text="Пароль", font="Arial 14")
lb_password.grid(row=2, column=0, pady=10)
e_password = Entry(root, width=30, font="Arial 14")
e_password.grid(row=2, column=1, pady=10)

lb_subject = Label(root, text="Тема", font="Arial 14")
lb_subject.grid(row=3, column=0, pady=10)
e_subject = Entry(root, width=30, font="Arial 14")
e_subject.grid(row=3, column=1, pady=10)

lb_text = Label(root, text="Cообщение", font="Arial 14")
lb_text.grid(row=4, column=0, pady=10)
text_text = Text(root, width=41, height=10)
text_text.grid(row=4, column=1, pady=10)

password = e_password.get()
from_ = e_from.get()
to_ = e_to.get()
subject = e_subject.get()
text = text_text.get(1.0, END)

btn_send = Button(root, text="Отправить", font="Arial 14", command=lambda: send_email(password, from_, to_, subject, text))
btn_send.grid(row=5, column=0, columnspan=2, sticky="ne")


root.mainloop()