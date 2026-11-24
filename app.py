
import streamlit as st

st.title("Hoes Simulator 😂")

st.write(
    "Good Morning Lil Folks (or afternoon depending on how long this takes me)\n\n"
    "Welcome to Hoes simulator to see if you can get hoes!"
)

st.header("First Question!")

q1 = st.radio(
    "You see the Hoes! What do you do?",
    [
        "A: Tell them your name",
        "B: Show them your bandz with your elite money spread",
        "C: Keep walking"
    ],
    key="q1"
)

if st.button("Submit Answer 1"):
    
    if q1.startswith("B"):
        st.success("Good job!")

        st.header("Next Question!")

        q2 = st.radio(
            "The hoes wanna do something. What should you take them to do?",
            [
                "A: Bowling",
                "B: Out to Eat",
                "C: To your place"
            ],
            key="q2"
        )

        if st.button("Submit Answer 2"):
            if q2.startswith("B"):
                st.success("Good job you know hoes love to eat 😂")

            elif q2.startswith("A"):
                st.error(
                    "Wrong answer you know hoes cant bowl\n\n"
                    "Try Again!"
                )

            elif q2.startswith("C"):
                st.error(
                    "WOOOOAH definitely scaring the hoes\n\n"
                    "Try Again!"
                )

    elif q1.startswith("A"):
        st.error(
            "AHHHH scaring the hoes they don't care who you are\n\n"
            "Try Again!"
        )

    elif q1.startswith("C"):
        st.error(
            "AHHH WRONG how u gon get the hoes???\n\n"
            "Try Again!"
        )
