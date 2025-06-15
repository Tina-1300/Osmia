import sys
import os
from dotenv import load_dotenv

load_dotenv()  # load content in file .env

email_sender = os.getenv('EMAIL_SENDER')  # get sender email
email_dest = os.getenv('EMAIL_DEST') # get email dest
email_password = os.getenv('EMAIL_PASSWORD')  # get application password
email_cc = os.getenv('cc') # destinataire de copie
email_bcc = os.getenv('cc') # destinataire de copie

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

list_files = [
    os.path.join(BASE_DIR, "random.hpp"),
    os.path.join(BASE_DIR, "libcurl-x64.dll"),
    os.path.join(BASE_DIR, "nasmdoc.pdf")
]

from Osmia.email_message import EmailMessage
from Osmia.email_config import EmailConfig
from Osmia.smtp_service_config import Gmail

gmail = Gmail()


# Configuration de l'email
config = EmailConfig(
    smtp_server=gmail.server, # server smtp
    smtp_port=gmail.port, # port smtp
    login=email_sender, # email de l'envoyeur 
    password=email_password # password d'application
)

# Création du mail
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

# envoie le même email à tout les email de la list to_email
responses = email.send_email(
    to_email=email_dest, # email du destinataire ou faire une list d'email de destinataire
    subject="Test Email format html",
    message=html_message, 
    type_email=str(format_mail[1]), # html => pour envoyer sous format html, plain => sous format text
    list_files=[list_files[0], list_files[2]], # 1 ou plusieur fichier cela fonctionne 
    email_service=gmail, # votre service smtp
    cc=email_cc # email destinataire copie
    #bcc=email_bcc # email destinataire copi caché
)


# peut garder cette syntax 
# response = email.send_email(
#     to_email=[email_dest, email_dest, email_dest], # email du destinataire ou faire une list d'email de destinataire
#     subject="Test Email format text",
#     message=text_message, 
#     type_email=str(format_mail[0]), # html => pour envoyer sous format html, plain => sous format text
#     list_files=[list_files[0]], # 1 ou plusieur fichier cela fonctionne
#     email_service=gmail votre service smtp
# )

