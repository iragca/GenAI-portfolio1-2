import streamlit as st
from pig_latin import translate as to_piglatin
import time

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

"""
langchain deprecation warning: 

Importing LLMs from langchain is deprecated. 
Importing from langchain will no longer be supported as of langchain==0.2.0. 
Please import from langchain-community instead:`from langchain_community.llms import HuggingFaceEndpoint`.
To install langchain-community run `pip install -U langchain-community`.
"""

import openai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
import langchain_mistralai

from langchain_community.chat_models.huggingface import ChatHuggingFace
from langchain_community.llms import HuggingFaceEndpoint

# endpoint_url = (
#     "https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2"
# )
# hf = HuggingFaceEndpoint(
#     # endpoint_url=endpoint_url,
#     repo_id="mistralai/Mistral-7B-Instruct-v0.2",
#     huggingfacehub_api_token=st.secrets["HUGGINGFACEHUB_API_TOKEN"]
# )



llm_mistral = HuggingFaceEndpoint(repo_id="mistralai/Mistral-7B-Instruct-v0.2")
"""Service (?) Error
InferenceTimeoutError: Model not loaded on the server: https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2. Please retry with a higher timeout (current: 120).
"""


llm_gemini = ChatGoogleGenerativeAI(model="gemini-pro")
llm_openai = ChatOpenAI() #OpenAI(model="gpt-3.5-turbo-instruct")
llm_mistralai = langchain_mistralai.ChatMistralAI(model="mistral-large-latest")



