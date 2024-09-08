import streamlit as st

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from langchain.llms import HuggingFaceEndpoint
"""
langchain deprecation warning: 

Importing LLMs from langchain is deprecated. 
Importing from langchain will no longer be supported as of langchain==0.2.0. 
Please import from langchain-community instead:`from langchain_community.llms import HuggingFaceEndpoint`.
To install langchain-community run `pip install -U langchain-community`.
"""
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import OpenAI

llm_mistral = HuggingFaceEndpoint(repo_id="mistralai/Mistral-7B-Instruct-v0.2")
llm_gemini = ChatGoogleGenerativeAI(model="gemini-pro")
llm_openai = OpenAI(model="gpt-3.5-turbo-instruct")