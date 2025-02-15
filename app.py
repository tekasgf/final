import streamlit as st
from modules.chains import process_query
from modules.memory import save_memory, get_memory, search_memory
from modules.telegram_bot import process_important_query

st.title("🤖 Final Project AI-бот")

if "last_input" not in st.session_state:
    st.session_state["last_input"] = None

user_input = st.text_input("Введите ваш вопрос:")

if user_input and user_input != st.session_state["last_input"]:
    # Проверяем, есть ли похожий запрос в памяти
    similar_responses = search_memory(user_input)

    if similar_responses != "Совпадений не найдено.":
        st.write("🔍 Найдено в памяти:")
        for response in similar_responses:
            st.write(f"💾 {response}")

    # Обрабатываем новый запрос
    response = process_query(user_input)

    # Сохраняем в память
    save_memory(user_input, response)

    # Отправляем уведомление, если запрос важный
    process_important_query(user_input)

    st.write("Ответ:", response)
    st.session_state["last_input"] = user_input

if st.button("Показать историю"):
    history = get_memory()
    if not history:
        st.write("История пуста.")
    else:
        st.write("### 📜 История общения:")
        for msg in history:
            if msg.type == "human":
                st.write(f"🧑‍💻 **Вы:** {msg.content}")
            else:
                st.write(f"🤖 **Бот:** {msg.content}")
            st.write("---")


if st.button("Новый вопрос"):
    st.session_state["last_input"] = None
