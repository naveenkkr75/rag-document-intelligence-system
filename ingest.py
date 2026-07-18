from dotenv import load_dotenv

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from langchain_community.document_loaders import (
    PyPDFDirectoryLoader,
    DirectoryLoader,
    TextLoader,
    Docx2txtLoader
)

from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

directory = "data/uploads"

pdf_docs = PyPDFDirectoryLoader(directory).load()

text_docs = DirectoryLoader(
    directory,
    glob="**/*.txt",
    loader_cls=TextLoader
).load()

docx_docs = DirectoryLoader(
    directory,
    glob="**/*.docx",
    loader_cls=Docx2txtLoader
).load()

docs = pdf_docs + text_docs + docx_docs

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(docs)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="vector_db/chroma_db"
)

print("Vector Database Created Successfully")