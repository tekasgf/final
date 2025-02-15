from langchain_ollama import OllamaLLM
from config import LLM_MODEL

# Запуск модели Ollama
llm = OllamaLLM(model=LLM_MODEL)

def generate_response(query):
    return llm.invoke(query)

