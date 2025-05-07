import os
import mimetypes
from email.mime.base import MIMEBase
from email import encoders
from .smtp_service_config import * 


class EmailAttachment:
    def __init__(self, file_path):
        self.file_path = file_path

    def attach_file(self, msg):
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f"The file '{self.file_path}' does not exist.")

        mimetype, _ = mimetypes.guess_type(self.file_path)
        if mimetype is None:
            raise ValueError("Error MimTypes not found")

        mime_main, mime_sub = mimetype.split("/")
        with open(self.file_path, "rb") as attachment:
            part = MIMEBase(mime_main, mime_sub)
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        filename = os.path.basename(self.file_path)  # To avoid sending the full path
        part.add_header("Content-Disposition", f"attachment; filename={filename}")
        msg.attach(part)