import streamlit as st
import requests

st.set_page_config(
    page_title="Enterprise RAG Platform",
    layout="wide"
)

st.title("Enterprise RAG Platform")

uploaded_files = st.file_uploader(
    "Upload PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    for uploaded_file in uploaded_files:

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                "application/pdf"
            )
        }

        response = requests.post(
            "http://127.0.0.1:8000/upload",
            files=files
        )

        if response.status_code != 200:
            st.error(response.text)

    st.success("All PDFs indexed successfully!")

query = st.text_input(
    "Ask a question"
)

if st.button("Search"):

    if not query.strip():
        st.warning("Please enter a question.")
        st.stop()

    response = requests.get(
        "http://127.0.0.1:8000/search",
        params={"query": query}
    )

    if response.status_code != 200:
        st.error(response.text)

    else:

        data = response.json()

        st.subheader("Answer")

        st.success(
            data.get(
                "answer",
                "No answer generated."
            )
        )

        if data.get("sources"):

            st.subheader("Sources")

            for source in set(data["sources"]):
                st.info(source)

        if data.get("retrieved_context"):

            with st.expander(
                "Retrieved Context"
            ):

                for item in data["retrieved_context"]:

                    if isinstance(item, dict):

                        st.write(
                            item.get(
                                "text",
                                ""
                            )
                        )

                    else:
                        st.write(item)

                    st.divider()