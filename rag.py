from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite"
)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = Chroma(
    persist_directory="vector_db/chroma_db",
    embedding_function=embeddings
)

while True:

    user_query = input("\nAsk Question (type exit to quit): ")

    if user_query.lower() == "exit":
        break

    retrieved_docs = vector_store.similarity_search(
        user_query,
        k=4
    )

    context = "\n".join(
        doc.page_content
        for doc in retrieved_docs
    )

    prompt = f"""
You are a helpful assistant.

Answer ONLY using the context below.

If the answer is unavailable, say:

I couldn't find that information in the uploaded documents.

Context:
{context}

Question:
{user_query}
"""

    response = llm.invoke(prompt)

    print("\nAnswer:\n")
    print(response.content)

    print("\nSources:")

    shown = set()

    for doc in retrieved_docs:

        source = doc.metadata.get("source", "Unknown")

        if source not in shown:
            print("-", source)
            shown.add(source)