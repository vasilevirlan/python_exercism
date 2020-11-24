import string as st
def is_pangram(sentence):
    alphabet = st.ascii_lowercase
    for letter in alphabet:
        if letter not in sentence.lower():
            return False
    return True
