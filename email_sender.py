from dotenv import load_dotenv
import os

load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")
PASSWORD = os.getenv("PASSWORD")


class EmailSender:
    def send_email(self, subject, email_message):
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        sender_email = SENDER_EMAIL
        receiver_email = RECEIVER_EMAIL
        password = PASSWORD

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        message.attach(MIMEText(email_message, "html"))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password) # type: ignore
            server.sendmail(sender_email, receiver_email, message.as_string()) # type: ignore
