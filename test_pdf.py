from app.loaders.pdf_loader import PDFLoader

loader = PDFLoader()

document = loader.load("data/sample.pdf")

print(document["file_name"])
print(document["type"])
print(document["content"][:500])