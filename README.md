# 🤖 Advanced AI Chatbot with Memory (Streamlit + LangChain + Ollama)

## 📖 Description
This project is an **interactive AI chatbot** capable of handling queries, maintaining conversation history, and sending **important notifications via Telegram**. It is built using **LangChain**, **Ollama**, and **Streamlit**.

🔹 **Project Features:**
- 💬 **Natural language processing** using **Ollama LLM**.
- 📂 **Short-term and long-term memory** with **ChromaDB**.
- ⚠️ **Detection of important queries** and **sending notifications to Telegram**.
- 🚀 **Profanity filtering**.
- 🎨 **User-friendly interface** powered by **Streamlit**.

---

## 🛠️ Installation & Setup

### 1️⃣ **Install Dependencies**
Ensure you have **Python 3.10+** installed. Then install dependencies:

pip install -r requirements.txt

Configure Settings

Edit the config.py file to add your Telegram Bot Token and Chat ID:

TELEGRAM_BOT_TOKEN = "YOUR_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"

Run the Application
After setup, launch the app:

streamlit run app.py

Now open your browser and visit http://localhost:8501.

Project Structure
📂 final_project/
│── 📜 app.py              # Main Streamlit app
│── 📜 config.py           # Configuration file
│── 📜 requirements.txt     # Dependency list
│── 📂 modules/             # Project modules
│   │── 📜 chains.py        # Query processing (LangChain)
│   │── 📜 llm_model.py     # Ollama LLM integration
│   │── 📜 memory.py        # Memory management (ChromaDB)
│   │── 📜 telegram_bot.py  # Telegram notifications

Features

📌 1. Query Processing
User queries are processed using LangChain (chains.py).
Profanity filtering replaces offensive words (SWEAR_WORDS in config.py).
📌 2. Memory Management
Short-term memory using ConversationBufferMemory.
Long-term memory with ChromaDB for storing chat history.
📌 3. Telegram Notifications
The bot sends alerts if a query contains important keywords (e.g., "urgent", "error").
Uses telegram_bot.py and asyncio.run() for async messaging.

🔗 Technologies Used

Streamlit – Interactive UI
LangChain – Data processing and memory management
Ollama LLM – AI-powered response generation
ChromaDB – Long-term memory storage
Telegram Bot API – Real-time notifications

💡 Future Improvements

Improve important query detection using AI.
Add chat history visualization in Streamlit.
Enhance memory handling with more context-aware processing.

Authors

Developer: Talgat Sagatov
Course / Project: Advanced Programming

Contact
🔗 GitHub: github.com/tekasgf






