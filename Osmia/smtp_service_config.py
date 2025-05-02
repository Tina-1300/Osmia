
class Gmail:
    def __init__(self):
        self.server = "smtp.gmail.com"
        self.port = 587
        self.size_max_file = 25 * 1024 * 1024  # 25 Mo

class Orange:
    def __init__(self):
        self.server = "smtp.orange.fr"
        self.port = 465

class SFR:
    def __init__(self):
        self.server = "smtp.sfr.fr"
        self.port = 465

class FREE:
    def __init__(self):
        self.server = "smtp.free.fr"
        self.port = 587

class Yahoo:
    def __init__(self):
        self.server = "smtp.mail.yahoo.com"
        self.port = 587

class Outlook:
    def __init__(self):
        self.server = "smtp.office365.com"
        self.port = 587