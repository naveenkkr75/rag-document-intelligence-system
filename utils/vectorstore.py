from langchain_chroma import Chroma

from config import DB_PATH

from utils.embeddings import get_embeddings


def get_vector_store():

    return Chroma(
        persist_directory=DB_PATH,
        embedding_function=get_embeddings()
    )