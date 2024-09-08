from initialization import * 


st.write("""
# Ask Apu anything

""")

user_query = st.text_input("Input here")

llm_response = llm_mistral.invoke(user_query)
piggie = to_piglatin(llm_response)
st.write(llm_response)
st.write(piggie)



decipher = "Can you decipher this pig latin text?" +"\n" + piggie

st.write(llm_gemini.invoke(decipher).content)