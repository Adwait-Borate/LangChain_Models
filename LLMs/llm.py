from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct')

result = llm.invoke("What is the capital of India")
# invoke is an impt method in langchain
print(result)

# since this is an LLM (not used these days) it takes string/text as input and also gives string/text as output