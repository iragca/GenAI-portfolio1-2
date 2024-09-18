import streamlit as st

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
    ("OpenAI", "MistralAI", "Gemini", "Phi"),
    index=None,
    placeholder="Select Chatbot",
    key=303
    )


    init_chat = st.button("Chat Now")
    if init_chat and this_option != None:
        st.session_state['chat_option'] = this_option
        st.session_state['main_init'] = True
        st.rerun()
    elif init_chat and this_option == None:
        st.error("Please select a chatbot.")
    
def init_session_vars(llm_name, prompt_schema=[]):
    st.header(f"{chat}")
    if f'{llm_name}_history' not in st.session_state:
        st.session_state[f"{llm_name}_history"] = []

    # instantiating a list to store the whole conversation so far for giving context and memory for the LLM
    if f"{llm_name}_messages" not in st.session_state:
        st.session_state[f"{llm_name}_messages"] = prompt_schema

if st.session_state['chat_option'] == "OpenAI":
    chat = st.session_state['chat_option']
    from OpenAI import display_chat_history
    from OpenAI import ask_openai as ask_llm
    init_session_vars("OpenAI", [SystemMessage(content="You are a helpful assistant.")])

if st.session_state['chat_option'] == "MistralAI":
    chat = st.session_state['chat_option']
    from MistralAI import display_chat_history
    from MistralAI import ask_mistralai as ask_llm
    init_session_vars("MistralAI", [("system", "You are a helpful assistant.")])

if st.session_state['chat_option'] == "Gemini":
    chat = st.session_state['chat_option']
    from Gemini import display_chat_history
    from Gemini import ask_gemini as ask_llm
    init_session_vars("Gemini", [])

####

if st.session_state['main_init']:
    option = st.sidebar.selectbox(
        "Switch chatbot",
        ("OpenAI", "MistralAI", "Gemini", "Phi"),
        index=None,
        placeholder="Switch Chatbot",
        key=302,
        label_visibility="collapsed"
    ) 

    switch_chat = st.sidebar.button("Switch Now")
    if switch_chat and option != None:
        st.session_state['chat_option'] = option
        st.rerun()
    elif switch_chat and option == None:
        st.sidebar.error("Please select a chatbot.")

    st.sidebar.markdown(" *** ")
    st.sidebar.header("Chat Settings")
    toggle_display_metadata = st.sidebar.toggle("Enable Response Metadata")
    toggle_display_timestamp = st.sidebar.toggle("Enable Message Age")

    user_query = st.chat_input(f"Ask {chat}")

    if user_query != None:
        start_time = time.time()
        answer = ask_llm(user_query)
        end_time = time.time()
        st.session_state[f'{chat}_history'].append((user_query, (start_time, end_time), answer))

    display_chat_history(response_metadata=toggle_display_metadata, message_age=toggle_display_timestamp)