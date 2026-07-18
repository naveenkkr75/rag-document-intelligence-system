import os
import streamlit as st

from dotenv import load_dotenv

from utils.llm import get_llm
from utils.vectorstore import get_vector_store
from utils.indexer import index_document
from utils.retriever import retrieve_documents
from utils.prompts import build_prompt
from utils.parser import parse_response


load_dotenv()

UPLOAD_FOLDER = "data/uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


st.set_page_config(
    page_title="RAG Document Intelligence System",
    page_icon="📄",
    layout="wide"
)


st.title("📄 RAG Document Intelligence System")
st.write("Upload documents and ask questions using Gemini + ChromaDB.")


# ------------------------
# Clear Chat
# ------------------------

if st.sidebar.button("Clear Chat"):

    st.session_state.messages = []

    st.rerun()


# ------------------------
# Initialize Chat Memory
# ------------------------

if "messages" not in st.session_state:

    st.session_state.messages = []


# ------------------------
# Upload Documents
# ------------------------

uploaded_files = st.file_uploader(
    "Upload PDF, TXT or DOCX",
    type=["pdf", "txt", "docx"],
    accept_multiple_files=True
)


if uploaded_files:

    for file in uploaded_files:

        save_path = os.path.join(
            UPLOAD_FOLDER,
            file.name
        )


        # Save file

        with open(save_path, "wb") as f:

            f.write(file.getbuffer())


        with st.spinner(f"Indexing {file.name}..."):

            indexed = index_document(save_path)


        if indexed:

            st.success(
                f"✅ {file.name} indexed successfully!"
            )

        else:

            st.warning(
                f"⚠️ {file.name} is already indexed."
            )


# ------------------------
# Load Models
# ------------------------

vector_store = get_vector_store()

llm = get_llm()


# ------------------------
# Display Chat History
# ------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])



# ------------------------
# Ask Question
# ------------------------

question = st.chat_input(
    "Ask something about your documents..."
)


if question:


    # Save user message

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )


    with st.chat_message("user"):

        st.write(question)



    # Retrieve documents

    docs = retrieve_documents(question)


    if len(docs) == 0:

        answer = (
            "I couldn't find that information "
            "in the uploaded documents."
        )


    else:


        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )


        prompt = build_prompt(
            context,
            question
        )


        with st.spinner("Thinking..."):

            response = llm.invoke(prompt)


        answer = parse_response(response)



    # Display assistant response

    with st.chat_message("assistant"):

        st.write(answer)



    # Save assistant message

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )


    # ------------------------
    # Sources
    # ------------------------

    if len(docs) > 0:

        with st.expander("Sources"):

            shown = set()


            for doc in docs:


                source = doc.metadata.get(
                    "source",
                    "Unknown"
                )


                if source not in shown:

                    st.write("•", source)

                    shown.add(source)