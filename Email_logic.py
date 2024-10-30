from email.message import EmailMessage
import smtplib
from tkinter import messagebox as mb

def send_email(password, from_, to_, subject, text):
    message = EmailMessage()
    message.set_content(text)
    message["From"] = from_
    message["To"] = to_
    message["Subject"] = subject
    server = None
    try:
        server = smtplib.SMTP_SSL("smtp.yandex.ru", 465)
        server.login(from_, password)
        server.send_message(message)
        mb.showinfo("Отправка e-mail", f"Сообщение с темой {subject} отправлено успешно.")
    except Exception as exc:
        mb.showerror("Ошибка при отправке e-mail!", f"Ошибка: {exc}")
    finally:
        if server:
            server.quit()

#send_email("ISPrevGR1_", "hauptmann11@yandex.ru", "7034052@gmail.com", "Test!!!", "This is test")