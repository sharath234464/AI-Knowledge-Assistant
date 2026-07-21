import requests
import streamlit as st

FASTAPI_URL = "http://127.0.0.1:8000"


def show_stats():

    try:

        response = requests.get(
            f"{FASTAPI_URL}/documents",
            timeout=30
        )

        if response.status_code != 200:
            st.error("Cannot load dashboard.")
            return

        documents = response.json()["documents"]

    except Exception as e:

        st.error(e)
        return

    total_documents = len(documents)

    total_chunks = sum(
        document["chunks"]
        for document in documents
    )

    pdf_count = sum(
        1
        for document in documents
        if document["file_type"] == "PDF"
    )

    docx_count = sum(
        1
        for document in documents
        if document["file_type"] == "DOCX"
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "📄 Documents",
            total_documents
        )

    with col2:
        st.metric(
            "🧩 Chunks",
            total_chunks
        )

    with col3:
        st.metric(
            "🤖 Embedding",
            "MiniLM"
        )

    with col4:
        st.metric(
            "🗄 Vector DB",
            "ChromaDB"
        )

    st.divider()

    st.subheader("📊 Document Types")

    chart_data = {
        "PDF": pdf_count,
        "DOCX": docx_count
    }

    st.bar_chart(chart_data)

    st.divider()

    st.subheader("📂 Uploaded Files")

    if total_documents == 0:

        st.info("No uploaded documents.")

    else:

        for document in documents:

            st.write(
                f"📄 **{document['filename']}**"
            )

            st.caption(
                f"{document['chunks']} chunks"
            )

    st.divider()

    st.subheader("ℹ️ System Information")

    st.success(
        """
Embedding Model : all-MiniLM-L6-v2

Vector Database : ChromaDB

LLM : GPT-4.1-mini
"""
    )