from datetime import datetime
import streamlit as st

from api import ask_question


def show_chat():

    st.subheader("💬 AI Knowledge Assistant")

    st.caption("Ask questions about your uploaded documents.")

    # -----------------------------
    # Session State
    # -----------------------------
    if "messages" not in st.session_state:
        st.session_state.messages = []

    col1, col2 = st.columns([8, 1])

    with col2:
        if st.button("🗑 Clear"):
            st.session_state.messages = []
            st.rerun()

    st.divider()

    # -----------------------------
    # Display Previous Messages
    # -----------------------------
    for message in st.session_state.messages:

        avatar = "👤" if message["role"] == "user" else "🤖"

        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])
            st.caption(message["time"])

    # -----------------------------
    # User Input
    # -----------------------------
    prompt = st.chat_input("Type your question...")

    if not prompt:
        return

    current_time = datetime.now().strftime("%I:%M %p")

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
            "time": current_time,
        }
    )

    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)
        st.caption(current_time)

    # Show assistant response
    with st.chat_message("assistant", avatar="🤖"):

        with st.spinner("Searching documents and generating answer..."):

            try:

                response = ask_question(prompt)

                if response.status_code == 200:

                    data = response.json()

                    answer = data.get("answer", "No answer received.")

                    st.markdown(answer)

                    st.caption(current_time)

                    st.info("📄 Answer generated from your uploaded knowledge base.")

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": answer,
                            "time": current_time,
                        }
                    )

                else:

                    st.error("Failed to get response from the server.")
                    st.code(response.text)

            except Exception as e:

                st.error("Unable to connect to the FastAPI server.")
                st.code(str(e))