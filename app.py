import streamlit as st
import pandas as pd
import altair as alt

st.title("My First Streamlit App")
st.write("Welcome to my dashboard!")

number = st.slider("Pick a number", 0, 100, 50)
st.write(f"You selected: {number}")

if st.button("Click me!"):
    st.write("Button clicked!")

data = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 20, 25, 20, 10]
})
chart = alt.Chart(data).mark_line().encode(x='x', y='y')
st.altair_chart(chart, use_container_width=True)
