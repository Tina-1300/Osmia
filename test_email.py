from Osmia.email_message import EmailMessage
from Osmia.email_config import EmailConfig

# Configuration de l'email
config = EmailConfig(
    smtp_server="smtp.gmail.com", # server smtp
    smtp_port=587, # port smtp
    login="email@gmail.com", # email de l'envoyeur 
    password="mot de passe d'application" # password d'application
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

response = email.send_email(
    to_email="destinataire@gmail.com", # email du destinataire 
    subject="Test Email",
    message=html_message, 
    type_email=str(format_mail[1]), # html => pour envoyer sous format html, plain => sous format text
    list_files=["random.hpp", "libcurl-x64.dll"] # 1 ou plusieur fichier cela fonctionne
)

