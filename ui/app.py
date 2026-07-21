import streamlit as st
from pathlib import Path

from components.sidebar import show_sidebar
from components.home import show_home
from components.chat import show_chat
from components.documents import show_documents
from components.stats import show_stats


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AI Knowledge Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================
# LOAD CSS
# ==========================================

def load_css():

    css_path = Path(__file__).parent / "styles" / "style.css"

    if css_path.exists():

        with open(css_path, "r", encoding="utf-8") as f:

            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )


load_css()


# ==========================================
# SIDEBAR
# ==========================================

page = show_sidebar()


# ==========================================
# HOME
# ==========================================

if page == "🏠 Home":

    show_home()


# ==========================================
# CHAT
# ==========================================

elif page == "💬 AI Chat":

    st.title("💬 AI Chat")

    st.write(
        "Ask questions based on your uploaded documents."
    )

    show_chat()


# ==========================================
# DOCUMENTS
# ==========================================

elif page == "📂 Documents":

    st.title("📂 Uploaded Documents")

    st.write(
        "Search, manage and delete uploaded files."
    )

    show_documents()


# ==========================================
# DASHBOARD
# ==========================================

elif page == "📊 Dashboard":

    st.title("📊 Analytics Dashboard")

    st.write(
        "View statistics of your knowledge base."
    )

    show_stats()


# ==========================================
# SETTINGS
# ==========================================

elif page == "⚙️ Settings":

    st.title("⚙️ Settings")

    st.info("Authentication Module Coming Soon")

    st.markdown("### Upcoming Features")

    st.checkbox("User Login", disabled=True)

    st.checkbox("User Registration", disabled=True)

    st.checkbox("Password Reset", disabled=True)

    st.checkbox("Dark Mode", disabled=True)

    st.checkbox("Notifications", disabled=True)

    st.checkbox("Chat Export", disabled=True)

    st.checkbox("Profile Settings", disabled=True)

    st.checkbox("Theme Customization", disabled=True)

    st.divider()

    st.success("Version 2.0")

    st.caption("Developed using FastAPI, LangChain, OpenAI, ChromaDB and Streamlit.")