import streamlit as st


def show_footer():

    st.divider()

    st.markdown(
        """
        <div style='text-align:center;padding:15px;color:gray;'>

        <b>AI Knowledge Assistant</b><br>

        Built using FastAPI • LangChain • OpenAI • ChromaDB • Streamlit

        </div>
        """,
        unsafe_allow_html=True,
    )