import streamlit as st

from components.hero import show_hero
from components.stats import show_stats
from components.footer import show_footer


def show_home():

    # ==========================================
    # HERO SECTION
    # ==========================================

    show_hero()

    # ==========================================
    # WELCOME
    # ==========================================

    st.header("🚀 Welcome")

    st.write(
        """
Welcome to the **AI Knowledge Assistant**.

This platform helps you upload your knowledge documents,
build an AI-powered knowledge base, and ask questions using
Retrieval-Augmented Generation (RAG).
"""
    )

    st.divider()

    # ==========================================
    # FEATURES
    # ==========================================

    st.header("✨ Features")

    col1, col2 = st.columns(2)

    with col1:

        st.success("📂 Upload Multiple Documents")

        st.success("🤖 AI Question Answering")

        st.success("📄 Document Management")

        st.success("🔍 Semantic Search")

    with col2:

        st.success("📊 Analytics Dashboard")

        st.success("🧠 ChromaDB Vector Search")

        st.success("⚡ GPT-4.1-mini Integration")

        st.success("📚 Enterprise Knowledge Base")

    st.divider()

    # ==========================================
    # SUPPORTED FILE TYPES
    # ==========================================

    st.header("📂 Supported File Types")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.info(
            """
📄 PDF

📄 DOCX

📄 TXT
"""
        )

    with c2:

        st.info(
            """
📄 CSV

📄 JSON

📄 HTML
"""
        )

    with c3:

        st.info(
            """
📄 Markdown

📄 Excel (.xlsx)

📄 PowerPoint (.pptx)
"""
        )

    st.caption(
        "Some formats require backend loaders to be implemented before uploads will work."
    )

    st.divider()

    # ==========================================
    # QUICK STATISTICS
    # ==========================================

    st.header("📈 Dashboard Overview")

    show_stats()

    # ==========================================
    # RECENT ACTIVITY
    # ==========================================

    st.header("🕒 Recent Activity")

    st.info("📄 Upload new documents to build your knowledge base.")

    st.info("💬 Ask questions using the AI Chat page.")

    st.info("📊 View analytics from the Dashboard.")

    st.divider()

    # ==========================================
    # TECHNOLOGY
    # ==========================================

    st.header("🛠 Technology Stack")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Backend", "FastAPI")

    with c2:
        st.metric("LLM", "GPT-4.1-mini")

    with c3:
        st.metric("Embedding", "MiniLM")

    with c4:
        st.metric("Vector DB", "ChromaDB")

    show_footer()