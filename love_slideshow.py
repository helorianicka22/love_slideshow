import streamlit as st
import time

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="For Someone Special 💖",
    page_icon="💖",
    layout="centered"
)

# -------------------------------------------------
# PASSWORD LOCK
# -------------------------------------------------
PASSWORD = "Onyet"   # 🔒 CHANGE THIS

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.markdown("## 🔒 Enter Password")
    pwd = st.text_input("Password", type="password")

    if st.button("Unlock ❤️"):
        if pwd == PASSWORD:
            st.session_state.authenticated = True
            st.success("Unlocked 💖")
            time.sleep(1)
            st.rerun()
        else:
            st.error("Wrong password 😢")
    st.stop()

# -------------------------------------------------
# SLIDES (EDIT TEXT ONLY)
# -------------------------------------------------
slides = [
    "💖 Hello my love.\n\nKu bosan shekali terkurung.Jadi, ku buat ini untukmu hehe.",
    "🌸 I just want you to know that you are deeply appreciated.",
    "✨ No matter what happens, my heart always finds its way back to you.",
    "💞 If life gives me a thousand choices, I will still choose you.",
]

# -------------------------------------------------
# SLIDE STATE
# -------------------------------------------------
if "slide" not in st.session_state:
    st.session_state.slide = 0

# -------------------------------------------------
# DISPLAY SLIDES OR ENDING
# -------------------------------------------------
if st.session_state.slide < len(slides):
    st.markdown(
        f"""
        <style>
        .slide {{
            animation: fadeIn 1.2s;
            text-align: center;
            padding: 50px;
            font-size: 26px;
        }}

        @keyframes fadeIn {{
            from {{opacity: 0; transform: translateY(30px);}}
            to {{opacity: 1; transform: translateY(0);}}
        }}
        </style>

        <div class="slide">
            {slides[st.session_state.slide]}
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.balloons()
    st.markdown(
        """
        <h1 style="text-align:center;">🎆 THE END 🎆</h1>
        <h3 style="text-align:center;">I love you, always 💖</h3>
        """,
        unsafe_allow_html=True
    )

# -------------------------------------------------
# NAVIGATION BUTTONS
# -------------------------------------------------
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.button("⬅️ Previous") and st.session_state.slide > 0:
        st.session_state.slide -= 1
        st.rerun()

with col3:
    if st.button("Next ➡️") and st.session_state.slide < len(slides):
        st.session_state.slide += 1
        st.rerun()

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.markdown(
    "<p style='text-align:center; color:grey;'>Made with ❤️</p>",
    unsafe_allow_html=True
)
