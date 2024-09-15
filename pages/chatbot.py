from initialization import *
import time

@st.cache_resource
def ask_gemini(user_prompt):
    return llm_gemini.invoke(user_prompt).content

history = []
# @st.cache_data
# def history(append):
#     history = []
#     history.append(append)
#     for chat in history:
#         st.write(chat)

if 'history' not in st.session_state:
    st.session_state['history'] = history



def display():
    for chat in st.session_state['history']:
        # st.write(st.session_state['history'])
        time_history = time.time() - chat[1]
        if time_history < 60:
            final_text = f"{time_history:.0f} seconds ago" if time_history > 1 else f"1 second ago"
        else:
            text = f"{time_history // 60:.0f} mins" if time_history // 60 > 1 else f"{time_history // 60:.0f} min"
            text2 = f"{time_history % 60:.0f} secs" if time_history % 60 > 1 else f"1 sec"
            final_text = f"{text} and {text2} ago"

        st.html(f"<img src=\"https://github.com/Chris-Gari/Global-Terrorism-EDA/blob/main/chatbot2.png?raw=true\" alt=\"Placeholder Image\" style=\"padding: 10px;\"\"><small style=\"opacity: 0.5;\">{final_text}</small>")
        # st.write(chat[0])

        st.html(f"<p  text-align: right; float: right;><span style=\"background-color: rgba(255, 255, 255, 0.1); padding-top: 10px; padding-bottom: 10px; padding-right: 15px; padding-left: 15px; border-radius: 20px;\">{chat[0]}</span></p>")
    

        st.html(f"<img src=\"https://github.com/Chris-Gari/Global-Terrorism-EDA/blob/main/chatbot.png?raw=true\" alt=\"Placeholder Image\" style=\"padding: 10px;\"\"> Gemini")
        st.write(chat[2])
        print(st.session_state['history'])





user_query = st.chat_input('Ask Gemini')

if user_query != None:
    answer = ask_gemini(user_query)
    st.session_state['history'].append((user_query, time.time(), answer))
    display()

