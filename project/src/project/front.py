import streamlit as st
from project import extractPage

# import extractPage
st.header("Welcome User, I am here to help you!")

st.write(
    "Upload a PDF document and extract its text quickly and easily. "
    "This tool reads the content of your PDF and displays the extracted text "
    "in a simple and user-friendly format."
)


file_type = st.radio(
    "Select your document type:",
    ["PDF", "DOCX"]
    
)


uploaded_file = st.file_uploader(
    "Upload your document",
    type=["pdf", "docx"]
)


if st.button("Parse"):

    if uploaded_file is not None:

        if file_type == "PDF":

            extracted_text = extractPage.extract_pdf(uploaded_file)

            st.subheader("Extracted Text")
            st.json(extracted_text)

        elif file_type == "DOCX":
             

            extracted_text = extractPage.extract_docx(uploaded_file)

            st.subheader("Extracted Text")
            st.json(extracted_text)

    else:
        st.warning("Please upload a document first.")
