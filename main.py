import streamlit as st
import os

# Set the title and description of the app
st.title("Document Search App")
st.write("Upload a document and search for keywords.")

# Upload a document
uploaded_file = st.file_uploader("Upload a document", type=["pdf", "txt"])

if uploaded_file is not None:
    # Display the uploaded document
    st.write("Uploaded document:")
    if uploaded_file.type == "application/pdf":
        st.write(f"PDF file: {uploaded_file.name}")
    elif uploaded_file.type == "text/plain":
        st.write(f"Text file: {uploaded_file.name}")

    # Read the content of the document
    if uploaded_file.type == "application/pdf":
        text = ""
        try:
            import PyPDF2
            pdf_reader = PyPDF2.PdfFileReader(uploaded_file)
            for page_num in range(pdf_reader.getNumPages()):
                text += pdf_reader.getPage(page_num).extractText()
        except Exception as e:
            st.error(f"Error reading PDF: {e}")
    elif uploaded_file.type == "text/plain":
        text = uploaded_file.read()

    # Search functionality
    st.subheader("Search")
    search_query = st.text_input("Enter a keyword to search:")
    if st.button("Search"):
        if search_query:
            # Perform the search
            search_results = [line for line in text.split('\n') if search_query in line]
            if search_results:
                st.subheader("Search Results:")
                for result in search_results:
                    st.write(result)
            else:
                st.write("No results found for the given keyword.")

    # Optionally, display the full document
    st.subheader("Full Document")
    st.write(text)

# Optionally, add additional features, like highlighting search results, etc.

