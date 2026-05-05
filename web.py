import streamlit as st
import os
from langchain_google_genai import ChatGoogleGenerativeAI,GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyMuPDFLoader,TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate

# PAGE TITLE
st.title("RAG Pipeline Using Gemini")


# API KEY
#key = os.getenv("gemini_key")

# LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",api_key='AIzaSyDg2drFHYL4xKWTIWbO14VWWb_79__AlEE')

# EMBEDDING MODEL
emb_llm = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001",google_api_key='AIzaSyDg2drFHYL4xKWTIWbO14VWWb_79__AlEE')


# FILE UPLOADER
file = st.file_uploader("Upload PDF or TXT File",type=["pdf", "txt"])


# PROCESS FILE
if file is not None:

    # Save uploaded file
    with open(file.name, "wb") as f:
        f.write(file.getbuffer())

    st.success(f"{file.name} uploaded successfully")


    # LOAD DOCUMENT
    try:
        if file.name.endswith(".pdf"):
            loader = PyMuPDFLoader(file.name)
        else:
            loader = TextLoader(
            file.name
            # encoding="utf-8"
            )
        docs = loader.load()

    except Exception as e:
        st.error(f"Error loading file: {e}")
        st.stop()

    # CHECK DOCUMENT
    if not docs:
        st.error("Document is empty")
        st.stop()

    # SPLIT DOCUMENT
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )
    chunks = splitter.split_documents(docs)


    # REMOVE EMPTY CHUNKS
    clean_chunks = []
    for chunk in chunks:
        text = chunk.page_content.strip()

        if text:
            clean_chunks.append(chunk)

    # CHECK CLEAN CHUNKS
    if len(clean_chunks) == 0:
        st.error("No readable text found in file")
        st.stop()

     # CREATE VECTOR STORE
    try:
        vs = FAISS.from_documents(
            documents=clean_chunks,
            embedding=emb_llm
        )

    except Exception as e:
        st.error(f"Embedding Error: {e}")
        st.stop()

    # USER QUESTION
    query = st.text_input("Ask Question")

    # QUESTION ANSWERING
    if query and query.strip():

        try:
         # Retriever
            retriever = vs.as_retriever(search_kwargs={"k": 5})
            rdocs = retriever.invoke(query)

            # Context
            context_text = "\n\n".join([doc.page_content for doc in rdocs])
            
            # Prompt
            prompt = PromptTemplate(
                template="""You are a helpful assistant.
                        Answer ONLY from the given context.
                        If answer is not available in context,
                        say:
                        "Information not found in document"
                        Context:{context}
                        Question:{question}""",
                input_variables=["context", "question"])

            # Chain
            chain = prompt | llm

            # Response
            response = chain.invoke({
                "context": context_text,
                "question": query
            })

            # Output
            st.subheader("Answer")
            st.write(response.content)

        except Exception as e:
            st.error(f"Error: {e}")