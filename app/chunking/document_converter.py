from langchain_core.documents import Document


class DocumentConverter:

    def convert(self, documents):
        """
        Preserve metadata from loaders.
        """

        converted = []

        for doc in documents:

            converted.append(
                Document(
                    page_content=doc.page_content,
                    metadata=doc.metadata
                )
            )

        return converted