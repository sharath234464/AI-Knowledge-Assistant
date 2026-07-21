import requests
import streamlit as st

FASTAPI_URL = "http://127.0.0.1:8000"


def show_documents():

    st.subheader("📄 Uploaded Documents")

    # Search Box
    search = st.text_input(
        "🔍 Search Documents",
        placeholder="Search by filename..."
    )

    st.write("")

    try:

        response = requests.get(
            f"{FASTAPI_URL}/documents",
            timeout=30
        )

        if response.status_code != 200:
            st.error("Unable to load documents.")
            return

        documents = response.json()["documents"]

    except Exception as e:

        st.error(str(e))
        return

    # Search Filter
    if search:

        documents = [
            doc
            for doc in documents
            if search.lower() in doc["filename"].lower()
        ]

    if len(documents) == 0:

        st.info("No matching documents found.")
        return

    st.write(f"### 📚 Total Documents : {len(documents)}")

    st.divider()

    for document in documents:

        col1, col2 = st.columns([8,1])

        with col1:

            if document["file_type"] == "PDF":
                icon = "📕"

            elif document["file_type"] == "DOCX":
                icon = "📘"

            elif document["file_type"] == "TXT":
                icon = "📄"

            elif document["file_type"] == "CSV":
                icon = "📊"

            else:
                icon = "📁"

            st.markdown(
                f"""
### {icon} {document['filename']}

**Type:** {document['file_type']}

**Chunks:** {document['chunks']}

**Uploaded:** {document['uploaded_at']}
"""
            )

        with col2:

            st.write("")

            st.write("")

            if st.button(
                "🗑 Delete",
                key=document["id"]
            ):

                delete = requests.delete(
                    f"{FASTAPI_URL}/documents/{document['id']}"
                )

                if delete.status_code == 200:

                    st.success("Deleted Successfully")

                    st.rerun()

                else:

                    st.error(delete.text)

        st.divider()