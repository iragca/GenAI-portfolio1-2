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
'## Demonstrating LLMs for decrypting weak encryption'

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



@st.cache_resource
def decrypt_base64(base64):
    personality = """
    Decrypt this base64 encoded string.\n\n
    """

    return llm_openai.invoke(personality + base64)

@st.cache_resource
def decrypt_SHA254(SHA256):
    personality = """
    Decrypt this SHA256 encoded string.\n\n
    """

    return llm_openai.invoke(personality + SHA256)

user_query = st.text_input('Ask Apu')
show_desc = False


if user_query != '':
    llm_answer = ask_apu(user_query)
    st.write(f"__Apu (mistralai/Mistral-7B-Instruct-v0.2)__ \n\n{llm_answer}")


    st.write("""
    ***
    """)
    st.write("__Encrypted Pig Latin message__ ")
    st.write(f"{to_piglatin(llm_answer)}")
    st.write("""
    ***
    """)
    '__Decrypting using OpenAI 3.5B Turbo model__'
    st.write(decrypt(to_piglatin(llm_answer)))
    show_desc = True

if show_desc:
    '\n\n'
    '### Observations'
    'Depending on luck and on the model, right now it _can_ partially decrypt a weak encryption like Pig Latin.'

'## Demonstrating LLMs for decrypting Base64'

import base64
sample_string = st.text_input('Encode to Base64')

if sample_string != '':

    sample_string_bytes = sample_string.encode("ascii")
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")

    '__Base64__'
    f'{base64_string}'
    ' *** '

    ascii_string = base64_string.encode("ascii")
    decoded_bytes = base64.b64decode(ascii_string)
    decoded_string = decoded_bytes.decode("ascii")

    openai_base64 = decrypt_base64(base64_string)

    '__Decrypting base64 using OpenAI 3.5b Turbo model__'

    f'{openai_base64}'


import hashlib
"## Let's try to do the impossible: Decoding SHA256"


sha_string = st.text_input('Encode to SHA256')
sha256_desc = False

if sha_string != '':
    '__SHA256__'

    hash256 = hashlib.sha256(bytes(sha_string, 'utf-8')).hexdigest()
    st.write(hash256)

    ' *** '

    llm_answer = decrypt_SHA254(hash256)

    st.write(llm_answer)
    sha256_desc = True

if sha256_desc:
    '\n\n'
    '### Observations'
    "The model and its guesses are not correct. Maybe it outright told you it can't decrypt SHA256"

    "Verdict: Generative AI can't decrypt strong encryption like SHA256, right now"
    'Can we train a model specifically for breaking SHA25? Pair a string with its encoded SHA256 message'
    'and store it inside memory or a database'