
import streamlit as st

st.title("🎸 Band Name Generator")

st.write("Welcome to the Band Name Generator!")

home = st.text_input(
    "What's the name of the city you grew up in?"
)

pet = st.text_input(
    "What's your pet's name?"
)

if st.button("Generate Band Name"):
    if home and pet:
        st.success(f"Your band name could be The {home} {pet}!")
    else:
        st.warning("Please answer both questions!")
