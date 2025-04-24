import streamlit as st

st.title("My First Streamlit App")
st.write("Welcome to my dashboard!")

number = st.slider("Pick a number", 0, 100, 50)
st.write(f"You selected: {number}")

if st.button("Click me!"):
    st.write("Button clicked!")
