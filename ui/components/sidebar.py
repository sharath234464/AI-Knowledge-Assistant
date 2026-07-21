import streamlit as st


def show_sidebar():

    st.sidebar.title("🤖 AI Knowledge Assistant")

    st.sidebar.caption("Enterprise RAG Platform")

    st.sidebar.divider()

    page = st.sidebar.radio(

        "Navigation",

        [

            "🏠 Home",

            "💬 AI Chat",

            "📂 Documents",

            "📊 Dashboard",

            "⚙️ Settings"

        ]

    )

    st.sidebar.divider()

    st.sidebar.success("🟢 Backend Connected")

    st.sidebar.info("🤖 Model\n\nGPT-4.1-mini")

    st.sidebar.info("🧠 Embedding\n\nall-MiniLM-L6-v2")

    st.sidebar.info("🗄 Vector DB\n\nChromaDB")

    st.sidebar.metric("📄 Documents", "2")

    st.sidebar.metric("🧩 Chunks", "77")

    st.sidebar.divider()

    st.sidebar.caption("Version 2.0")

    return page