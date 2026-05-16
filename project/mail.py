import smtplib
from email.message import EmailMessage
import os

def send_email(user_email, verify_link):
    message = EmailMessage()
    message['Subject'] = "Підтвердження акаунту"
    message["From"] = os.getenv("EMAIL")
    message['To'] = user_email
    html = f"""
            <h1>Підтвердження акаунту</h1>
            <p>Натисніть на кнопку нижче для підтвердження акаунту</p>
            <a href="{verify_link}">Підтвердити акаунт</a>
            """
    message.add_alternative(html, subtype='html')
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.starttls()
        smtp.login(os.getenv("EMAIL"), os.getenv("EMAIL_PASSWORD"))
        smtp.send_message(message)