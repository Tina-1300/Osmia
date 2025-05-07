class Gmail:
    def __init__(self):
        self.server = "smtp.gmail.com" # smpt name server
        self.port = 587 # smtp port server
        self.size_max_file = 25 * 1024 * 1024  # 25 Mo

class Orange:
    def __init__(self):
        self.server = "smtp.orange.fr" # smtp name server
        self.port = 465 # smtp port server
        self.size_max_file = 25 * 1024 * 1024  # 25 Mo

class SFR:
    def __init__(self):
        self.server = "smtp.sfr.fr" # smtp name server
        self.port = 465 # smtp port server
        self.size_max_file = 15 * 1024 * 1024  # 15 Mo

class Yahoo:
    def __init__(self):
        self.server = "smtp.mail.yahoo.com" # smtp name server
        self.port = 587 # smtp port server
        self.size_max_file = 25 * 1024 * 1024 # 25 Mo

class Outlook:
    def __init__(self):
        self.server = "smtp.office365.com" # smtp name server
        self.port = 587 # smtp port server
        self.size_max_file = 10 * 1024 * 1024 # 10 Mo pour un abbonement personel et 20 Mo pour un professionel
        # ajouter une vérification pour vérifier si l'adresse de l'envoyeur et perso ou pro pour palier 
        # à ce problème

