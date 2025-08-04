import streamlit as st
from nltk.chat.util import Chat, reflections

# Chatbot pairs
pairs = [
    ["hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    ["how are you?", ["I'm great, thanks!", "Doing well, how about you?"]],
    ["what is your name?", ["I'm a chatbot!"]],
    ["bye", ["Goodbye!", "See you soon!"]],
    [".*", ["I'm not sure I understand that."]]
]

chatbot = Chat(pairs, reflections)

# Streamlit interface
st.title("💬 Simple Chatbot")
user_input = st.text_input("You:")

if user_input:
    response = chatbot.respond(user_input)
    st.markdown(f"*Bot:* {response}")
