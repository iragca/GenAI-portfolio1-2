from initialization import *
from langchain.text_splitter import CharacterTextSplitter
st.set_page_config(page_title="Chris Irag", page_icon="♿")

code = st.text_area(label='IDE', height=720,)


prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")


text_splitter = CharacterTextSplitter(chunk_size = 30, chunk_overlap = 10)

st.write(text_splitter.split_text(code))

st.sidebar.write("""
__Mistral__ 
***
""")


def llm_response(prompt):
    personality = "You will act as my autocomplete for my python code. Please don't worry about additional comments."
    return llm_mistral.invoke(prompt)



st.write(llm_response(code))

## TODO: implement overlay chat for mistral autocomplete AI IDE

## TODO: look for other implementations using langchain

## TODO: look into this https://huggingface.co/amazon/chronos-t5-tiny