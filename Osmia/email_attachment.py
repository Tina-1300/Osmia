import mimetypes
from email.mime.base import MIMEBase
from email import encoders

class EmailAttachment:
    def __init__(self, file_path):
        self.file_path = file_path

    def attach_file(self, msg):
        mimetype, _ = mimetypes.guess_type(self.file_path)
        if mimetype is None:
            raise ValueError("Error MimTypes not found")

        mime_main, mime_sub = mimetype.split("/")
        with open(self.file_path, "rb") as attachment:
            part = MIMEBase(mime_main, mime_sub)
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename={self.file_path}")
        msg.attach(part)
