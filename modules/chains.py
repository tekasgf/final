from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from modules.llm_model import generate_response
from config import SWEAR_WORDS

# Фильтрация нецензурных слов
def filter_input(text):
    for word in SWEAR_WORDS:
        text = text.replace(word, "***")
    return text

# Создаем промпт-шаблон
template = PromptTemplate(
    input_variables=["question"],
    template="Ответь на следующий вопрос: {question}"
)

# Создаем цепочку
def process_query(question):
    clean_question = filter_input(question)
    return generate_response(clean_question)
