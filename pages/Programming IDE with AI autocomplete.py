from initialization import *

code = st.text_area(label='IDE', height=720,)


prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")

## TODO: implement overlay chat for mistral autocomplete AI IDE