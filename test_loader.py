from app.loaders.universal_loader import UniversalLoader

loader = UniversalLoader()

document = loader.load("data/sample.pdf")

print(document)