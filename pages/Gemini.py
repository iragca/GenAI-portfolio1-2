from initialization import *
from langchain.schema import AIMessage, HumanMessage, SystemMessage

#llama-server --hf-repo bartowski/Phi-3.5-mini-instruct-GGUF --hf-file ./Phi-3.5-mini-instruct-Q5_K_M.gguf -c 512 

# initializing chat history as session state
if 'gemini_history' not in st.session_state:
    st.session_state['gemini_history'] = []


st.warning('PROGRESS WILL BE LOST when closing this session. This prototype is session-based.', icon="⚠️")
st.info('This prototype recommends using Dark Mode.', icon="ℹ️")

## display chat history using HTML
### Looking for more efficient ways to display chat history instead of a for loop!
def display_chat_history():
    for chat in st.session_state['gemini_history']:

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

        # Token summary
        tokens = chat[2].usage_metadata
        prompt_tokens = tokens['input_tokens']
        completion_tokens = tokens["output_tokens"]
        total_tokens = tokens["total_tokens"]

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
        <img src="./app/static/images/chatbot/gemini.webp" alt="Placeholder Image" style="padding: 5px; border-radius: 10px; background-color: rgb(255, 255, 255, 0.10); max-height: 32px; max-width: 100%; height: auto; width: auto;">
        <small style="opacity: 0.5; padding: 10px;">"""
            +f"Gemini"
        """</small>
        """)

        ## Token Summary
        st.html(f"""
        <small style="opacity: 0.5;">"""
            +f"Model: N/A <br>Prompt Tokens: {prompt_tokens} | Completion Tokens: {completion_tokens} | Total Tokens: {total_tokens}"
        """</small>
        """)

        st.markdown(f"{chat[2].content}")
        

user_query = st.chat_input('Ask Gemini')

# @st.cache_resource
# def ask_gemini(user_prompt):
#     st.session_state["gemini_messages"].append([{"user": user_prompt}])
#     assistant_answer = llm_gemini.invoke(user_prompt)
#     st.session_state["gemini_messages"].append([{"assistant": assistant_answer.content}])
#     return assistant_answer
# gemini will block ChatBot prompting. will block for 'block_reason: 2'

# instantiating a list to store the whole conversation so far for giving context and memory for the LLM

if "gemini_messages" not in st.session_state:
    st.session_state["gemini_messages"] = [{"system": "You are a helpful assistant."}]

@st.cache_resource
def ask_gemini(user_prompt):
    return llm_gemini.invoke(user_prompt)

if user_query != None:
    answer = ask_gemini(user_query)
    st.session_state['gemini_history'].append((user_query, time.time(), answer))

display_chat_history()



# st.session_state["gemini_history"]