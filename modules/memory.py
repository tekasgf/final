import chromadb
from langchain.memory import ConversationBufferMemory
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.openai import OpenAIEmbeddings
from langchain_community.docstore.in_memory import InMemoryDocstore

# Инициализируем ChromaDB
chroma_client = chromadb.PersistentClient(path="./chroma_db")  # Сохраняем базу локально
collection = chroma_client.get_or_create_collection(name="chat_memory")

# Память с использованием LangChain
memory = ConversationBufferMemory(return_messages=True)

# Функция для добавления в память
def save_memory(question, response):
    memory.save_context({"input": question}, {"output": response})
    collection.add(
        documents=[question], 
        metadatas=[{"response": response}], 
        ids=[str(len(collection.get()["ids"]))]
    )

# Получение истории диалога
def get_memory():
    return memory.load_memory_variables({})["history"]

# Поиск в памяти
def search_memory(query):
    results = collection.query(query_texts=[query], n_results=3)
    return results["documents"] if results["documents"] else "Совпадений не найдено."
