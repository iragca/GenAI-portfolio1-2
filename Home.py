from initialization import * 
st.set_page_config(page_title="Chris Irag", page_icon="♿")

st.write(
"""
# Portfolio 1
This project is made by Chris Irag of DS3A


## Generative AI
""")

# st.navigation([st.Page("Home.py")])

st.page_link("Home.py", label="Home", icon="🏠")
st.page_link("pages/Chatroom.py", label="Chatroom", icon="🤖")
# st.page_link("pages/LLMs for Decryption.py", label="LLMs for Decryption", icon="🤖")
# st.page_link("pages/Programming IDE with AI autocomplete.py", label="Programming IDE with AI autocomplete", icon="💻")
st.page_link("pages/README.py", label="README", icon="☑")
