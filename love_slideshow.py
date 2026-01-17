import streamlit as st
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="For Someone Special 💖",
    page_icon="💖",
    layout="centered"
)

# ---------------- PASSWORD LOCK ----------------
PASSWORD = "mylove123"  # 🔒 change if you want

if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.markdown("## 🔒 Enter Password")
    pwd = st.text_input("Password", type="password")

    if st.button("Unlock ❤️"):
        if pwd == PASSWORD:
            st.session_state.auth = True
            st.success("Unlocked 💖")
            time.sleep(1)
            st.rerun()
        else:
            st.error("Wrong password 😢")
    st.stop()

# ---------------- SLIDES TEXT ----------------
slides = [
    "💖 Haliuuu my baby onyett sayang",
    "This is something special, made only for you.",
    "No matter what happens, my heart always chooses you.",
    "Thank you for being my happiness.",
    "I love you, always 💕"
]

if "slide" not in st.session_state:
    st.session_state.slide = 0

# ---------------- CSS STYLES ----------------
st.markdown(
    """
    <style>
    .heart {
        width: 280px;
        height: 280px;
        background-image: url("IMG_20230728_120619_627.jpg");
        background-size: cover;
        background-position: center;
        position: relative;
        margin: 40px auto 20px auto;
        transform: rotate(-45deg);
        animation: pulse 1.8s infinite;
        box-shadow: 0 0 30px rgba(255, 105, 180, 0.9);
    }

    .heart::before,
    .heart::after {
        content: "";
        width: 280px;
        height: 280px;
        background-image: url("IMG_20230728_120619_627.jpg");
        background-size: cover;
        background-position: center;
        border-radius: 50%;
        position: absolute;
    }

    .heart::before {
        top: -140px;
        left: 0;
    }

    .heart::after {
        left: 140px;
        top: 0;
    }

    @keyframes pulse {
        0% { transform: rotate(-45deg) scale(1); }
        50% { transform: rotate(-45deg) scale(1.06); }
        100% { transform: rotate(-45deg) scale(1); }
    }

    .text-box {
        text-align: center;
        font-size: 26px;
        margin-top: 20px;
        animation: fadeIn 0.6s ease-in;
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- DISPLAY ----------------
if st.session_state.slide < len(slides):

    # ❤️ HEART
    st.markdown("<div class='heart'></div>", unsafe_allow_html=True)

    # 💬 STATIC TEXT (NO MOVEMENT)
    st.markdown(
        f"<div class='text-box'>{slides[st.session_state.slide]}</div>",
        unsafe_allow_html=True
    )

else:
    # 🎆 ENDING
    st.balloons()
    st.markdown(
        """
        <h1 style="text-align:center;">🎆 THE END 🎆</h1>
        <h3 style="text-align:center;">Thank you for being my everything 💖</h3>
        """,
        unsafe_allow_html=True
    )

# ---------------- NAVIGATION ----------------
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.button("⬅️ Previous") and st.session_state.slide > 0:
        st.session_state.slide -= 1
        st.rerun()

with col3:
    if st.button("Next ➡️") and st.session_state.slide < len(slides):
        st.session_state.slide += 1
        st.rerun()

# ---------------- FOOTER ----------------
st.markdown(
    "<p style='text-align:center; color:grey;'>Made with ❤️</p>",
    unsafe_allow_html=True
)
