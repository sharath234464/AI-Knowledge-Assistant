import streamlit as st

from api import upload_document


def show_upload():

    st.header("📂 Upload Documents")

    uploaded_files = st.file_uploader(
        "Choose one or more files",
        accept_multiple_files=True
    )

    if st.button("📤 Upload Documents"):

        if not uploaded_files:
            st.warning("Please select at least one file.")
            return

        progress = st.progress(0)

        for index, uploaded_file in enumerate(uploaded_files):

            try:

                response = upload_document(uploaded_file)

                if response.status_code == 200:

                    st.success(
                        f"✅ {uploaded_file.name} uploaded successfully."
                    )

                else:

                    st.error(response.text)

            except Exception as e:

                st.error(str(e))

            progress.progress((index + 1) / len(uploaded_files))

    st.markdown("---")