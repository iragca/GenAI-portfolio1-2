from initialization import * 


st.header("LLMs for Decryption")
st.subheader("An alternative solution to non-bijective and non-reversible encryption", divider="gray")

"""
This page is for showcasing one of the existing solutions to decrypting non-[bijective](https://en.wikipedia.org/wiki/Bijection) encryption and non-reversible encryption.
I will be showcasing this solution using [Pig Latin](https://en.wikipedia.org/wiki/Pig_Latin#Rules) as the encoder.

Why Pig Latin for two reasons:

- Two inputs can output the same value (non-bijective)
- Some information are lost upon encoding (You'll see later) (??)
- It is a poor way to encrypt data



##### -> So it only works on weak encryption?

Although this solution can't go against powerful non-reversible encryption like SHA-256 or MD5, I think it is still worth showcasing for the following reasons:

- Maybe in the future, innovations will prove this contemporary fact wrong.
- Hopefully, you can take away some useful insights.

***
"""

