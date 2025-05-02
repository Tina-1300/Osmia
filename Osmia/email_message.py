from .base_email import BaseEmail
from .email_attachment import EmailAttachment
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailMessage:
    def __init__(self, smtp_server, smtp_port, login, password):
        self.base_email = BaseEmail(smtp_server, smtp_port, login, password)

    def create_message(self, to_email, subject, message, type_email="plain"):
        msg = MIMEMultipart()
        msg["From"] = self.base_email.login
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(message, type_email))
        return msg

    def add_attachments(self, msg, list_files):
        for file in list_files:
            attachment = EmailAttachment(file)
            attachment.attach_file(msg)
        return msg

    def send_email(self, to_email, subject, message, type_email="plain", list_files=[]):
        if isinstance(to_email, str):
            msg = self.create_message(to_email, subject, message, type_email)
            if list_files:
                msg = self.add_attachments(msg, list_files)
            return self.base_email.send(to_email, msg)
        
        elif isinstance(to_email, list):
            results = []
            for email in to_email:
                msg = self.create_message(email, subject, message, type_email)
                if list_files:
                    msg = self.add_attachments(msg, list_files)
                result = self.base_email.send(email, msg)
                results.append((email, result))
            return results
        else:
            return False