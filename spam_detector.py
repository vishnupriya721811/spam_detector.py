import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from win32com.client import Dispatch
import numpy as np
#make streamlit documentation
#https://docs.streamlit.io/en/stable/api.html#display-charts

def speak(text):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(text)
model = pickle.load(open('spam.pkl', 'rb'))
cv = pickle.load(open('vectorizer.pkl', 'rb'))
pipe = pickle.load(open('Naive_model.pkl', 'rb'))

model = pickle.load(open('spam.pkl', 'rb'))
cv = pickle.load(open('vectorizer.pkl', 'rb'))

def main():
    st.title("Email Spam Classification Application")
    st.write("Built with Streamlit & Python")
    activities = ["Classification", "About"]
    choices = st.sidebar.selectbox("Select Activities", activities)

    if choices == "Classification":
        st.subheader("Classification")
        msg = st.text_area("Enter a text", height=200)

        if st.button("Process"):
            # Preprocess and transform the input data using the same vectorizer
            data = [msg]


            # Predict the labels using the trained model
            result = pipe.predict(data)[0]


            if result == 0:
                st.success("This is Not A Spam Email")
                speak("This is Not A Spam Email")
            else:
                st.error("This is A Spam Email")
                speak("This is A Spam Email")

if __name__ == '__main__':
    main()