import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY"),
)

def generate_answer(question: str) -> str:
    prompt = f"""
    You are a customer support assistant.

    Answer the user's question clearly and concisely.

    User question:
    {question}
    """

    response = llm.invoke(prompt)

    return response.content