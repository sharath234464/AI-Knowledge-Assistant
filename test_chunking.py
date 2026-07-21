from app.loaders.universal_loader import UniversalLoader

from app.chunking.text_splitter import TextChunker


loader = UniversalLoader()

document = loader.load("data/sample.pdf")


chunker = TextChunker()

chunks = chunker.split(document["content"])


print(f"Total Chunks : {len(chunks)}\n")


for i, chunk in enumerate(chunks):

    print("=" * 60)

    print(f"Chunk {i+1}")

    print("=" * 60)

    print(chunk[:400])

    print()