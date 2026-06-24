
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from  langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

print("\n Select The LLM You Need to use")

print("\n 1. Gemini Model")
print("\n 2. OpenAI Model")


llm_model = input("")

if llm_model == '1':
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    def connect_llm() -> ChatGoogleGenerativeAI:
        llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        api_key=GOOGLE_API_KEY
    )
        print("\n Connected to Gemini AI")
        return llm
    
elif llm_model == '2':
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    def connect_llm() -> ChatOpenAI:
        llm = ChatOpenAI(
        model="gpt-4o-mini",
        api_key=OPENAI_API_KEY
    )
        return llm
    
else:
    print("\n You did not select the Any model thank-you")

