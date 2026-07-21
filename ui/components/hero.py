import streamlit as st


def show_hero():

    st.markdown("""
<div class="hero-container">
<h1>🤖 AI Knowledge Assistant</h1>
<div class="hero-subtitle">Enterprise Retrieval-Augmented Generation Platform</div>
<div class="hero-description">Upload Documents • Search Knowledge • Ask Questions • Get AI Answers</div>
</div>
""", unsafe_allow_html=True)

    st.write("")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.success("📂 Upload")

    with c2:
        st.info("💬 Chat")

    with c3:
        st.warning("📄 Documents")

    with c4:
        st.error("📊 Dashboard")

    st.divider()