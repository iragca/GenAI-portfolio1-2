from initialization import *

## display chat history using HTML
### Looking for more efficient ways to display chat history instead of a for loop!
def display_chat_history(response_metadata=False, message_age=False):
    for chat in st.session_state['Phi_history']:

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

        # Token summary
        model = chat[2].model
        ct, pt, tk = chat[2].usage
        _usage_metadata(tk)

        ## User profile image and nam
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
        if response_metadata:
            st.html(f"""
            <small style="opacity: 0.5;">"""
                +f"Model: {model} <br>Prompt Tokens: {pt[1]} | Completion Tokens: {ct[1]} | Total Tokens: {tk[1]} <br>Processing Time: {process_time:.2f}"
            """</small>
            """)

        ## LLM Response

        st.markdown(f"{chat[2].choices[0].message.content}".replace("\\n", ""))

client = openai.OpenAI(
    #base_url="http://localhost:8080",
    base_url="http://172.28.110.188:8080",
    # base_url="http://192.168.1.100:5001/v1",
    api_key = "sk-no-key-required"
)

@st.cache_resource
def ask_phi(query):
    st.session_state["Phi_messages"].append({"role": "user", "content": query})
    completion = client.chat.completions.create(
        model="Phi-3.5-mini-instruct-Q8_0",
        messages = st.session_state["Phi_messages"]
    )
    st.session_state["Phi_messages"].append({"role": "assistant", "content": completion.choices[0].message.content})
    return completion

def usage_metadata():
    chat = st.session_state["Phi_history"][-1]
    ct, pt, tk = chat[2].usage
    st.session_state["Phi_usage"].append(tk)