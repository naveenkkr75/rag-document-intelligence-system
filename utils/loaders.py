from langchain_community.document_loaders import (
    PyPDFDirectoryLoader,
    DirectoryLoader,
    TextLoader,
    Docx2txtLoader,
)

from config import DATA_PATH


def load_documents():

    pdf_docs = PyPDFDirectoryLoader(
        DATA_PATH
    ).load()

    txt_docs = DirectoryLoader(
        DATA_PATH,
        glob="**/*.txt",
        loader_cls=TextLoader
    ).load()

    docx_docs = DirectoryLoader(
        DATA_PATH,
        glob="**/*.docx",
        loader_cls=Docx2txtLoader
    ).load()

    return pdf_docs + txt_docs + docx_docs