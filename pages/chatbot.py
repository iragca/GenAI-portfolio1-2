from initialization import *
from langchain.schema import AIMessage, HumanMessage, SystemMessage


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
        <small style="opacity: 0.5;">
            Mistral
        </small>
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


if "sessionMessages" not in st.session_state:
    st.session_state["sessionMessages"] = [SystemMessage(content="")]
    
@st.cache_resource
def load_answer(question):
    st.session_state["sessionMessages"].append(HumanMessage(content=question))
    assistant_answer = llm_mistralai.invoke(st.session_state["sessionMessages"])
    st.session_state["sessionMessages"].append(AIMessage(content=assistant_answer.content))

    return assistant_answer.content


if user_query != None:
    answer = load_answer(user_query)
    st.session_state['history'].append((user_query, time.time(), answer))

display_chat_history()
st.write(st.session_state["sessionMessages"])



