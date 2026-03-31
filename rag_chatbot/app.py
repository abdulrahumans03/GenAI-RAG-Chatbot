import streamlit as st
from loader import load_and_split
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import os

os.environ["OPENAI_API_KEY"] = "your-api-key"

st.title("GenAI Document Q&A (RAG)")

uploaded_file = st.file_uploader("Upload PDF")

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    docs = load_and_split("temp.pdf")

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)

    st.success("Document processed successfully!")

    query = st.text_input("Ask a question")

    if query:
        docs = vectorstore.similarity_search(query)

        chain = load_qa_chain(OpenAI(), chain_type="stuff")
        answer = chain.run(input_documents=docs, question=query)

        st.subheader("Answer")
        st.write(answer)