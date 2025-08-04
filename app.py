import streamlit as st
import nltk
import speech_recognition as sr
from nltk.chat.util import Chat, reflections

# Load chatbot data
pairs = [
    ["hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    ["how are you?", ["I'm doing great, thanks!", "All good! How can I help?"]],
    ["what is your name?", ["I'm a chatbot."]],
    ["bye", ["Goodbye!", "See you later!"]],
    [".*", ["Sorry, I didn't understand that. Can you say it again?"]]
]

chatbot = Chat(pairs, reflections)

# Function to recognize speech
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Please speak now.")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            st.success(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            st.error("Sorry, I could not understand the audio.")
        except sr.RequestError:
            st.error("Speech Recognition service is unavailable.")
    return ""

# Streamlit UI
st.title("🗣 Speech-Enabled Chatbot")

input_type = st.radio("Choose input type:", ("Text", "Speech"))

user_input = ""

if input_type == "Text":
    user_input = st.text_input("Type your message:")
elif input_type == "Speech":
    if st.button("Start Talking"):
        user_input = recognize_speech()

if user_input:
    response = chatbot.respond(user_input)
    st.markdown(f"*Bot:* {response}")
    