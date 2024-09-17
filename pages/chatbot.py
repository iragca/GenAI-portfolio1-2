from initialization import *
from langchain.schema import AIMessage, HumanMessage, SystemMessage

#llama-server --hf-repo bartowski/Phi-3.5-mini-instruct-GGUF --hf-file ./Phi-3.5-mini-instruct-Q5_K_M.gguf -c 512 

# initializing chat history as session state
if 'history' not in st.session_state:
    st.session_state['history'] = []


st.warning('PROGRESS WILL BE LOST when closing this session. This prototype is session-based.', icon="⚠️")
st.info('This prototype recommends using Dark Mode.', icon="ℹ️")

## display chat history using HTML
### Looking for more efficient ways to display chat history instead of a for loop!
def display_chat_history():
    for chat in st.session_state['history']:

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
            +f"Mistral (Tokens used: {1})"
        """</small>
        """)

        ## LLM Response
        # st.html("""
        # <div style="text-align: left;">
        #     <div style="text-align: left; display: inline-block; padding-top: 10px; padding-bottom: 10px; padding-right: 15px; padding-left: 15px; border-radius: 20px; overflow-wrap: break-word;">"""
        #         +f"{chat[2]}"+
        #     """</div>
 
        # </div>
        # """)

        st.markdown(f"{chat[2]}")
        

user_query = st.chat_input('Ask Mistral')

@st.cache_resource
def ask_mistral(query):
    return llm_mistral.invoke(query)

@st.cache_resource
def ask_gemini(user_prompt):
    return llm_gemini.invoke(user_prompt).content


# instantiating a list to store the whole conversation so far for giving context and memory for the LLM
if "sessionMessages" not in st.session_state:
    #st.session_state["sessionMessages"] = [SystemMessage(content="You are a helpful assistant.")]
    #st.session_state["sessionMessages"] = [("system", "You are a helpful assistant.")]
    st.session_state["sessionMessages"] = [{"role": "system", "content": "You are a helpful assistant."}]

@st.cache_resource
def ask_openai(question):
    st.session_state["sessionMessages"].append(HumanMessage(content=question))
    assistant_answer = llm_openai.invoke(st.session_state["sessionMessages"])
    st.session_state["sessionMessages"].append(AIMessage(content=assistant_answer.content))
    return assistant_answer

@st.cache_resource
def ask_mistralai(question):
    st.session_state["sessionMessages"].append(("human", question))
    assistant_answer = llm_mistralai.invoke(st.session_state["sessionMessages"])
    st.session_state["sessionMessages"].append(("assistant", assistant_answer.content))
    return assistant_answer




import openai

client = openai.OpenAI(
    # base_url="http://localhost:8080",
    base_url="http://192.168.1.100:5001/v1",
    api_key = "sk-no-key-required"
)



def local_phi():
	
	completion = client.chat.completions.create(
    model="Phi-3.5-mini-instruct-Q5_K_M",
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What a lovely day today, right?"}
    ]
	)
	
	return completion

@st.cache_resource
def ask_phi(query):

    st.session_state["sessionMessages"].append({"role": "user", "content": query})
    completion = client.chat.completions.create(
        model="Phi-3.5-mini-instruct-Q5_K_M",
        messages = st.session_state["sessionMessages"]
    )

    return completion

if user_query != None:
    answer = ask_phi(user_query)
    st.session_state['history'].append((user_query, time.time(), answer))

display_chat_history()
# st.write(st.session_state["sessionMessages"])



