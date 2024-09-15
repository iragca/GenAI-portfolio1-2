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

st.warning('PROGRESS WILL BE LOST when closing this session. This prototype is session-based.', icon="⚠️")
st.info('This prototype recommends using Dark Mode.', icon="ℹ️")


def display():
    for chat in st.session_state['history']:
        # st.write(st.session_state['history'])
        time_history = time.time() - chat[1]
        if time_history < 60:
            final_text = f"{time_history:.0f} seconds ago" if time_history > 1 else f"1 second ago"
        else:
            text = f"{time_history // 60:.0f} mins" if time_history // 60 > 1 else f"{time_history // 60:.0f} min"
            text2 = f"{time_history % 60:.0f} secs" if time_history % 60 > 1 else f"1 sec"
            final_text = f"{text} {text2} ago"

        # st.html(f"<img src=\"https://github.com/Chris-Gari/Global-Terrorism-EDA/blob/main/chatbot2.png?raw=true\" alt=\"Placeholder Image\" style=\"padding: 10px;\"\"><small style=\"opacity: 0.5;\">{final_text}</small>")
        # # st.write(chat[0])

        # st.html(f"<p  text-align: right; float: right;><span style=\"background-color: rgba(255, 255, 255, 0.1); padding-top: 10px; padding-bottom: 10px; padding-right: 15px; padding-left: 15px; border-radius: 20px;\">{chat[0]}</span></p>")
    

        # st.html(f"<img src=\"https://github.com/Chris-Gari/Global-Terrorism-EDA/blob/main/chatbot.png?raw=true\" alt=\"Placeholder Image\" style=\"padding: 10px;\"\"> Gemini")
        # st.write(chat[2])

        st.html("""
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Align Inline Elements Right</title>
        <style>
            .container {
                text-align: right; /* Aligns inline elements inside to the right */
                padding: 0px; /* Padding around the content */
            }
            .container span {
                padding: 10px; /* Padding around the text */
                border-radius: 20px; /* Rounded corners */
            }
            </style>
        </head>
        <body>
            <div class="container">"""+f"<small style=\"opacity: 0.5;\">{final_text}</small>"+
                """<img src=\"https://github.com/Chris-Gari/Global-Terrorism-EDA/blob/main/chatbot2.png?raw=true\" alt=\"Placeholder Image\" style=\"padding: 10px; border-radius: 20px;\">"""+
                """
            </div>
        </body>
        """)
        st.html(f"<div class=\"container\" ><p text-align: right; float: right;><span style=\"background-color: #d5547f; padding-top: 10px; padding-bottom: 10px; padding-right: 15px; padding-left: 15px;\">{chat[0]}</span></p></div>")
        st.html(f"<img src=\"https://github.com/Chris-Gari/Global-Terrorism-EDA/blob/main/chatbot.png?raw=true\" alt=\"Placeholder Image\" style=\"padding: 10px; border-radius: 20px;\"\"> Gemini")
        st.write(chat[2])



user_query = st.chat_input('Ask Gemini')

if user_query != None:
    answer = "Answer" #ask_gemini(user_query)
    st.session_state['history'].append((user_query, time.time(), answer))
    display()

