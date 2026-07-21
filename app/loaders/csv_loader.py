import pandas as pd


class CSVLoader:

    def load(self, file_path):

        df = pd.read_csv(file_path)

        text = df.to_string(index=False)

        return {
            "content": text,
            "type": "csv"
        }