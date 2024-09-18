from initialization import *
from langchain.schema import AIMessage, HumanMessage, SystemMessage

## display chat history using HTML
### Looking for more efficient ways to display chat history instead of a for loop!
def display_chat_history(response_metadata=False, message_age=False):
    for chat in st.session_state['OpenAI_history']:

        ## timestamp
        process_time = chat[1][1] - chat[1][0]
        time_history = time.time() - chat[1][0]

        if message_age:
            if time_history < 60:
                final_text = f"{time_history:.0f} seconds ago" if time_history > 2 else "Now"
            else:
                mins = time_history // 60
                secs = time_history % 60
                text = f"{mins:.0f} mins" if mins > 1 else f"1 min"
                text2 = f"{secs:.0f} secs" if secs > 1 else f"1 sec"
                final_text = f"{text} {text2} ago"
        else:
            final_text = "User"

        model = chat[2].response_metadata["model_name"]
        tokens = chat[2].response_metadata["token_usage"]
        prompt_tokens = tokens["prompt_tokens"]
        completion_tokens = tokens["completion_tokens"]
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
        <img src="./app/static/images/chatbot/openai.webp" alt="Placeholder Image" style="padding: 5px; border-radius: 10px; background-color: rgb(255, 255, 255, 0.90); max-height: 32px; max-width: 100%; height: auto; width: auto;">
        <small style="opacity: 0.5; padding: 10px;">"""
            +f"OpenAI"
        """</small>
        """)


        ## Token Summary
        if response_metadata:
            st.html(f"""
            <small style="opacity: 0.5;">"""
                +f"Model: {model} <br>Prompt Tokens: {prompt_tokens} | Completion Tokens: {completion_tokens} | Total Tokens: {total_tokens} <br>Processing Time: {process_time:.2f}"
            """</small>
            """)

        ## LLM Response
        st.markdown(f"{chat[2].content}")
        
@st.cache_resource
def ask_openai(question):
    st.session_state["OpenAI_messages"].append(HumanMessage(content=question))
    assistant_answer = llm_openai.invoke(st.session_state["OpenAI_messages"])
    st.session_state["OpenAI_messages"].append(AIMessage(content=assistant_answer.content))
    return assistant_answer

