from pathlib import Path

from app.loaders.pdf_loader import PDFLoader
from app.loaders.docx_loader import DocxLoader
from app.loaders.txt_loader import TxtLoader
from app.loaders.csv_loader import CSVLoader
from app.loaders.html_loader import HTMLLoader
from app.loaders.json_loader import JSONLoader


class UniversalLoader:

    def __init__(self):

        self.loaders = {
            ".pdf": PDFLoader(),
            ".docx": DocxLoader(),
            ".txt": TxtLoader(),
            ".csv": CSVLoader(),
            ".html": HTMLLoader(),
            ".json": JSONLoader(),
        }

    def load(self, file_path):

        extension = Path(file_path).suffix.lower()

        loader = self.loaders.get(extension)

        if loader is None:
            raise ValueError(f"Unsupported file type: {extension}")

        return loader.load(file_path)