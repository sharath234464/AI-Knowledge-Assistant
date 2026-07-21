import json


class JSONLoader:

    def load(self, file_path):

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        return {
            "content": json.dumps(data, indent=2),
            "type": "json"
        }