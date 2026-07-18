def build_prompt(context, question):

    return f"""
You are a helpful AI assistant.

Answer ONLY using the provided context.

If the answer is not found, say:

"I couldn't find that information in the uploaded documents."

Context:
{context}

Question:
{question}
"""