from initialization import *
from langchain.schema import AIMessage, HumanMessage, SystemMessage
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Chris Irag", page_icon="♿")

st.sidebar.info("Usage Summary feature is Work in Progress")
supported_llms = ("OpenAI", "MistralAI", "Gemini", "Phi", "Llama")

#llama-server --hf-repo bartowski/Phi-3.5-mini-instruct-GGUF --hf-file Phi-3.5-mini-instruct-Q4_0_4_4.gguf -c 4096

if 'main_init' not in st.session_state:
    st.session_state['main_init'] = False

if 'chat_option' not in st.session_state:
    st.session_state['chat_option'] = None

if not st.session_state['main_init']:
    st.markdown("""
    # Chatroom
    ### by Chris Irag, DS3A
    
    ***
    """)
    this_option = st.selectbox(
    "Who would you like to talk to?",
    supported_llms,
    index=None,
    placeholder="Select Chatbot",
    key=303
    )



    enable_switching_init = True if this_option == None else False
    init_chat = st.button("Chat Now", disabled=enable_switching_init, help='Choose a chatbot to chat with')
    
    if init_chat:
        st.session_state['chat_option'] = this_option
        st.session_state['main_init'] = True
        st.rerun()
    
def init_session_vars(llm_name, prompt_schema=[]):
    st.header(f"{chat}")
    if f'{llm_name}_history' not in st.session_state:
        st.session_state[f"{llm_name}_history"] = []

    # instantiating a list to store the whole conversation so far for giving context and memory for the LLM
    if f"{llm_name}_messages" not in st.session_state:
        st.session_state[f"{llm_name}_messages"] = prompt_schema

    if f"{llm_name}_usage" not in st.session_state:
        st.session_state[f"{llm_name}_usage"] = []

if st.session_state['chat_option'] == "OpenAI":
    chat = st.session_state['chat_option']
    from OpenAI import display_chat_history
    from OpenAI import ask_openai as ask_llm
    from OpenAI import usage_metadata
    init_session_vars("OpenAI", [SystemMessage(content="You are a helpful assistant.")])

if st.session_state['chat_option'] == "MistralAI":
    chat = st.session_state['chat_option']
    from MistralAI import display_chat_history
    from MistralAI import ask_mistralai as ask_llm
    from MistralAI import usage_metadata
    init_session_vars("MistralAI", [("system", "You are a helpful assistant.")])

if st.session_state['chat_option'] == "Gemini":
    chat = st.session_state['chat_option']
    from Gemini import display_chat_history
    from Gemini import ask_gemini as ask_llm
    from Gemini import usage_metadata
    init_session_vars("Gemini", [])


if st.session_state['chat_option'] == "Phi":
    chat = st.session_state['chat_option']
    from Phi import display_chat_history
    from Phi import ask_phi as ask_llm
    from Phi import usage_metadata
    init_session_vars("Phi", [{"role": "system", "content": "You are a helpful assistant."}])

####

if st.session_state['main_init']:
    try:
        option = st.sidebar.selectbox(
            "Switch chatbot",
            ("OpenAI", "MistralAI", "Gemini", "Phi", "Llama"),
            index=None,
            placeholder="Switch Chatbot",
            key=302,
            label_visibility="collapsed"
        ) 

        enable_switching = True if option == None else False
        switch_chat = st.sidebar.button("Switch Now", disabled=enable_switching, help='Choose a chatbot to switch to')
        
        if switch_chat:
            st.session_state['chat_option'] = option
            st.rerun()


        #TODO: apply area chart input and output tokens
        @st.dialog("Usage Summary")
        def summary(chat):
            chats = {
                "Total Tokens": st.session_state[f'{chat}_usage'],
                "Message Number": [x for x in range(1, len(st.session_state[f'{chat}_usage'])+1)]
            }
            st.area_chart(data=pd.DataFrame(chats), x="Message Number", y="Total Tokens")

        st.sidebar.markdown(" *** ")

        st.sidebar.header("Chat Settings")
        st.session_state["toggle_display_metadata"] = st.sidebar.toggle("Enable Response Metadata")
        st.session_state["toggle_display_timestamp"] = st.sidebar.toggle("Enable Message Age")
                  
        user_query = st.chat_input(f"Ask {chat}")

        if user_query != None:
            start_time = time.time()
            answer = ask_llm(user_query)
            end_time = time.time()
            st.session_state[f'{chat}_history'].append((user_query, (start_time, end_time), answer))
            usage_metadata()

        display_chat_history(response_metadata=st.session_state["toggle_display_metadata"], message_age=st.session_state["toggle_display_timestamp"])


        st.sidebar.markdown(" *** ")
        if st.sidebar.button("Usage Summary", disabled=len(st.session_state[f'{chat}_usage']) == 0, help="Display available usage information"):
            summary(chat)
        

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.info("""
        ## Please ...

        ### Report

        - If you think this is a bug.

        """)
        st.link_button("Report a Bug", "Report_a_Bug", type="primary")

        st.info("""
        ### Wait
        - Service is not available and should be available soon.
        - If this feature is yet to be supported.
        """)
