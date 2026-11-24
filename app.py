
import streamlit as st

st.title("Hoe Simulator")

st.write(
    "How goes it fellows\n\n"
    "Welcome to Hoe Simulator!\n\n"
    "To see if you can get Hoes!"
)

# Initialize game
if "question" not in st.session_state:
    st.session_state.question = 1

if "result" not in st.session_state:
    st.session_state.result = ""

def answer(next_question, message):
    st.session_state.result = message
    st.session_state.question = next_question

def restart():
    st.session_state.question = 1
    st.session_state.result = ""

# QUESTION 1
if st.session_state.question == 1:

    st.subheader("First Question!")
    st.write("You see the Hoes! What do you do?")

    st.button(
        "A: Tell them your name",
        on_click=answer,
        args=(4, "AHHHH scaring the hoes they don't care who you are\nHoes Lost Try Again!")
    )

    st.button(
        "B: Show them your bandz with your elite money spread",
        on_click=answer,
        args=(2, "Good Job you know hoes love the flex!")
    )

    st.button(
        "C: Keep walking",
        on_click=answer,
        args=(4, "AHHH WRONG how u gon get the hoes???\nHoes Lost Try Again!")
    )

# QUESTION 2
elif st.session_state.question == 2:

    st.subheader("Next Question!")
    st.write("The hoes wanna do something. What should you take them to do?")

    st.button(
        "A: Bowling",
        on_click=answer,
        args=(4, "Wrong answer you know hoes cant bowl\nHoes Lost Try Again!")
    )

    st.button(
        "B: Out to Eat",
        on_click=answer,
        args=(3, "Good job you know hoes love to eat")
    )

    st.button(
        "C: To your place",
        on_click=answer,
        args=(4, "WOOOOAH definelty scaring the hoes\nHoes Lost Try Again!")
    )

# QUESTION 3
elif st.session_state.question == 3:

    st.subheader("Last Question!")
    st.write("The Hoes wanna slide back to the crib! How do you bag the hoes?")

    st.button(
        "A: Show them your card collection",
        on_click=answer,
        args=(4, "HOES SECURED this young fellow knows how to get hoes")
    )

    st.button(
        "B: Whip it Out",
        on_click=answer,
        args=(4, "WHOOOOOAH definetley scaring the hoes\nHoes Lost Try again!")
    )

    st.button(
        "C: Watch a movie with them",
        on_click=answer,
        args=(4, "AHHHHH bored the hoes they left\nHoes Lost Try again!")
    )

# SHOW RESULTS
if st.session_state.result:

    st.write("---")
    st.write(st.session_state.result)

# GAME OVER / RESTART
if st.session_state.question == 4:

    st.button("Play Again 🔄", on_click=restart)
