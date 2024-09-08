import streamlit as st

st.write("""
# README

## Project Description

### Introduction

...

##  Running the App locally

### API Keys
If you want to run this app locally,
refer to this [streamlit documentation](https://docs.streamlit.io/develop/concepts/connections/secrets-management). It talks about how to manage your secrets/API keys.


### Web Server IP address
The web server port will always be 8501. 
Otherwise if that port is not available, it will be incremented by 1. (8501, 8502, ...)

""")
st.sidebar.markdown("""
# README
""")