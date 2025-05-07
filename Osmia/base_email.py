import smtplib
from email.mime.multipart import MIMEMultipart

class BaseEmail:
    def __init__(self, smtp_server, smtp_port, login, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.login = login
        self.password = password

    def send(self, to_email: str, msg: MIMEMultipart) -> str:
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.login, self.password)
                server.sendmail(self.login, to_email, msg.as_string())
        except Exception as e:
            return f"Error sending email : {e}"
