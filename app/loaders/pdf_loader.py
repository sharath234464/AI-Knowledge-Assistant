from pypdf import PdfReader

from app.loaders.base_loader import BaseLoader


class PDFLoader(BaseLoader):

    def load(self, file_path: str):

        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return {
            "file_name": file_path,
            "content": text,
            "type": "pdf"
        }