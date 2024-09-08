import streamlit as st

# import os
# os.environ["OPENAI_API_KEY"] = ""
# os.environ["GOOGLE_API_KEY"] = ""
# os.environ["HUGGINGFACEHUB_API_TOKEN"] = ""

from langchain.llms import HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import OpenAI

llm_mistral = HuggingFaceEndpoint(repo_id="mistralai/Mistral-7B-Instruct-v0.2")
llm_gemini = ChatGoogleGenerativeAI(model="gemini-pro")
llm_openai = OpenAI(model="gpt-3.5-turbo-instruct")
