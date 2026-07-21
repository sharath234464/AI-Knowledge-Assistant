from bs4 import BeautifulSoup


class HTMLLoader:

    def load(self, file_path):

        with open(file_path, "r", encoding="utf-8") as f:
            html = f.read()

        soup = BeautifulSoup(html, "html.parser")

        return {
            "content": soup.get_text(separator="\n"),
            "type": "html"
        }