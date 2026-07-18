from config import TOP_K
from utils.vectorstore import get_vector_store


def retrieve_documents(question):

    vector_store = get_vector_store()

    return vector_store.similarity_search(
        question,
        k=6
    )