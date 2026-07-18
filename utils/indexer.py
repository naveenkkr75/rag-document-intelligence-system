import os

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader,
)

from utils.file_tracker import (
    is_indexed,
    add_file,
)

from utils.vectorstore import get_vector_store
from utils.splitter import get_splitter


def index_document(file_path):

    # Skip if already indexed
    if is_indexed(file_path):
        return False

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        loader = PyPDFLoader(file_path)

    elif extension == ".txt":
        loader = TextLoader(file_path)

    elif extension == ".docx":
        loader = Docx2txtLoader(file_path)

    else:
        raise ValueError(f"Unsupported file type: {extension}")

    # Load document
    documents = loader.load()

    # Split into chunks
    splitter = get_splitter()
    chunks = splitter.split_documents(documents)

    # Load vector database
    vector_store = get_vector_store()

    # Add new chunks
    vector_store.add_documents(chunks)

    # Save file hash
    add_file(file_path)

    return True