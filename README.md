# Osmia

An ultra-simple and SOLID Python library for sending emails with attachments and HTML or plain text support.

---

## ✨ Features
- Send emails with plain text or HTML
- Easily add multiple attachments
- SOLID-compliant architecture
- Simple and clean interface
- sending email to a recipient email list
- adding different SMTP services : Gmail, Orange, SFR, Yahoo, Outlook
- adding cc and cci (bcc) 


---

## 🚀 Installation

```bash
git clone https://github.com/Tina-1300/Osmia.git
```
or 
```bash 
pip install osmia
```

example usage of library :

```python
from Osmia.email_message import EmailMessage
from Osmia.email_config import EmailConfig
from Osmia.smtp_service_config import Gmail

# configuration class of its SMTP provider
gmail = Gmail()

# Email Configuration
config = EmailConfig(
    smtp_server=gmail.server, # SMTP server
    smtp_port=gmail.port, # SMTP port
    login="email@gmail.com", # sender's email
    password="application password" # application password
)

# Creation of the email
email = EmailMessage(
    config.smtp_server,
    config.smtp_port,
    config.login,
    config.password
)

html_message = """
<html>
    <body>
        <h1 style="color:blue;">Ceci est un test HTML !</h1>
        <p>Envoi d'un email en <b>HTML</b> avec une pièce jointe.</p>
    </body>
</html>
"""

text_message = "Ceci est un test."

format_mail = ["plain", "html"]

files_listes = ["random.hpp", "libcurl-x64.dll", "nasmdoc.pdf"]


# sends the same email to all emails in the to_email list
responses = email.send_email(
    to_email=["destinatere@gmail.com", "destinatere2@gmail.com", "destinatere3@gmail.com"], # recipient email or make a recipient email list
    subject="Test Email html format",
    message=html_message, 
    type_email=str(format_mail[1]), # html => to send in html format, plain => in text format
    list_files=files_listes, # 1 or more files it works
    email_service=gmail, # your SMTP service
    bcc="tiers@gmail.com"
    #cc="tierse@gmail.com"
)

# we can keep this syntax
response = email.send_email(
    to_email="destinatere@gmail.com", # recipient email or make a recipient email list
    subject="Test Email text format",
    message=text_message, 
    type_email=str(format_mail[0]), # html => to send in html format, plain => in text format
    list_files=files_listes, # 1 or more files it works
    email_service=gmail # your SMTP service
)

# Please note that sending large files does not work.
```