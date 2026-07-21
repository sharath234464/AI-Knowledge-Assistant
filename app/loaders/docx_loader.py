from docx import Document


class DocxLoader:

    def load(self, file_path: str):

        doc = Document(file_path)

        text = []

        for paragraph in doc.paragraphs:
            if paragraph.text.strip():
                text.append(paragraph.text)

        return {
            "content": "\n".join(text),
            "type": "docx"
        }