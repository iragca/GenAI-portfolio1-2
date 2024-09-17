from initialization import *
from langchain.schema import AIMessage, HumanMessage, SystemMessage

#llama-server --hf-repo bartowski/Phi-3.5-mini-instruct-GGUF --hf-file ./Phi-3.5-mini-instruct-Q5_K_M.gguf -c 512 

# initializing chat history as session state
if 'phi_history' not in st.session_state:
    st.session_state['phi_history'] = []

# instantiating a list to store the whole conversation so far for giving context and memory for the LLM
if "phi_messages" not in st.session_state:
    st.session_state["phi_messages"] = [{"role": "system", "content": 'You are a helpful assistant.'}]


st.warning('PROGRESS WILL BE LOST when closing this session. This prototype is session-based.', icon="⚠️")
st.info('This prototype recommends using Dark Mode.', icon="ℹ️")

## display chat history using HTML
### Looking for more efficient ways to display chat history instead of a for loop!
def display_chat_history():
    for chat in st.session_state['phi_history']:

        ## timestamp
        time_history = time.time() - chat[1]
        if time_history < 60:
            final_text = f"{time_history:.0f} seconds ago" if time_history > 1 else "Now"
        else:
            mins = time_history // 60
            secs = time_history % 60
            text = f"{mins:.0f} mins" if mins > 1 else f"1 min"
            text2 = f"{secs:.0f} secs" if secs > 1 else f"1 sec"
            final_text = f"{text} {text2} ago"


        # tokens = chat[2].response_metadata["token_usage"]
        # total_tokens = tokens["total_tokens"]

        # Token summary
        model = chat[2].model
        ct, pt, tk = chat[2].usage
        ## User profile image and name
        st.html("""
        <div STYLE="text-align: right;">
            <small style="opacity: 0.5;">"""
            +f"{final_text}"+
            """</small>
            <img src="./app/static/images/chatbot/user.png" alt="Placeholder Image" style="padding: 10px; border-radius: 20px;">
        </div>
        """)

        ## User prompt
        st.html("""
        <div style="text-align: right; overflow-wrap: break-word;">
            <div style="text-align: left; background-color: rgb(213, 84, 127, 0.25); display: inline-block; padding-top: 10px; padding-bottom: 10px; padding-right: 15px; padding-left: 15px; border-radius: 20px; overflow-wrap: break-word;">"""
                +f"{chat[0]}"+
            """</div>
        </div>
        """)

        ## LLM profile image and name
        st.html(f"""
        <img src="./app/static/images/chatbot/chatbot1.png" alt="Placeholder Image" style="padding: 10px; border-radius: 20px;">
        <small style="opacity: 0.5;">"""
            +f"Phi"
        """</small>
        """)

        ## Token Summary
        st.html(f"""
        <small style="opacity: 0.5;">"""
            +f"Model: {model} <br>Prompt Tokens: {pt[1]} | Completion Tokens: {ct[1]} | Total Tokens: {tk[1]}"
        """</small>
        """)

        ## LLM Response

        st.markdown(f"{ chat[2].choices[0].message.content}")

user_query = st.chat_input('Ask Phi')

client = openai.OpenAI(
    # base_url="http://localhost:8080",
    base_url="http://192.168.1.100:5001/v1",
    api_key = "sk-no-key-required"
)



@st.cache_resource
def ask_phi(query):

    st.session_state["phi_messages"].append({"role": "user", "content": query})
    completion = client.chat.completions.create(
        model="Phi-3.5-mini-instruct-Q8_0",
        messages = st.session_state["phi_messages"]
    )
    st.session_state["phi_messages"].append({"role": "assistant", "content": completion.choices[0].message.content})
    return completion

if user_query != None:
    answer = ask_phi(user_query)
    st.session_state['phi_history'].append((user_query, time.time(), answer))
    

display_chat_history()