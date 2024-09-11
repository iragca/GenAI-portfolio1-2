from initialization import * 


st.header("LLMs for Decryption")
st.subheader("Can LLMs be an alternative solution for decryption?", divider="gray")

"""
This page is for showcasing one of the existing solutions to decrypting non-[bijective](https://en.wikipedia.org/wiki/Bijection) encryption and non-reversible encryption.
I will be showcasing this solution using [Pig Latin](https://en.wikipedia.org/wiki/Pig_Latin#Rules) as the encoder.

Why Pig Latin for two reasons:

- Two inputs can output the same value (non-bijective)
- Some information are lost upon encoding/decoding (You'll see later)
- It is a poor way to encrypt data



##### -> So it only works on weak encryption?

Although this solution can't go against powerful non-reversible encryption like SHA-256 or MD5, I think it is still worth showcasing for the following reasons:

- Maybe in the future, innovations will prove this contemporary fact wrong.
- Hopefully, you can take away some useful insights.

***
"""

st.image('assets/images/apu1.jpeg')

"""
__This is Apu.__

He is powered by Mistral (mistralai/Mistral-7B-Instruct-v0.2).
You can ask him anything but beware, he is not that good at talking.

"""


@st.cache_resource
def ask_apu(query):
    personality = """
    You will play the role of Chatbot, your personality should be Apu the frog.
    You don't talk like a frog, don't say things such as 'ribbit', but act like human.
    You are smart but act a little autistic. You refer to people as 'frens' or 'fren'.
    You are not energetic. You will not assume any prompts as and of the user.
    The following will be text prompts asked by the user. You should response fitting to your Apu personality.\n
    """

    return llm_gemini.invoke(personality + query).content


@st.cache_resource
def decrypt(piglatin_sequence):
    personality = """
    You will have to translate this Pig Latin sequence back into English. And nothing else.\n
    """

    return llm_openai.invoke(personality + piglatin_sequence)


user_query = st.text_input('Ask Apu')


llm_answer = ask_apu(user_query)

st.write(llm_answer)

st.write(to_piglatin(llm_answer))

st.write(decrypt(to_piglatin(llm_answer)))

st.write('asdfhkah')