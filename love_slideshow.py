import streamlit as st
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="For Someone Special 💖",
    page_icon="💖",
    layout="centered"
)

# ---------------- PASSWORD LOCK ----------------
PASSWORD = "mylove123"  # 🔒 CHANGE THIS

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

# ---------------- SLIDES DATA ----------------
slides = [
    {
        "title": "💖 Hello My Baby Onyettt Sayanggg",
        "text": "This is something special, made only for onyettttt.",
        "image": "https://drive.google.com/file/d/16bxwMSRCYPHydV2KZ1vAOL_PrAazdwpS/view?usp=sharing"
    },
    {
        "title": "🌸 A Gentle Reminder",
        "text": "Onyettt sayang are appreciated by me more than you will ever know.",
        "image": "https://drive.google.com/file/d/15Xj_Pu16YdbvvpsbjqhY2UKoTo63ZGXB/view?usp=sharing"
    },
    {
        "title": "✨ No Matter What Nyettt nyettt",
        "text": "Distance, time, pain or silence — my heart always finds you.",
        "image": "https://drive.google.com/file/d/1cz2tGTenAW1AiXJrPf1NnYBEUdpjPhTK/view?usp=sharing"
    },
    {
        "title": "💞 Always Onyettt Sayanggg",
        "text": "If life lets me choose again, I will still choose you.",
        "image": "https://drive.google.com/file/d/1O2h1vcnjsMGshL9Mi2Dn_Y9vBm9yEUB6/view?usp=sharing"
    }
]

# ---------------- SLIDE STATE ----------------
if "slide" not in st.session_state:
    st.session_state.slide = 0

# ---------------- ANIMATED SLIDE ----------------
slide = slides[st.session_state.slide]

st.markdown(
    f"""
    <style>
    .slide {{
        animation: fadeIn 1.2s;
        text-align: center;
        padding: 30px;
    }}

    @keyframes fadeIn {{
        from {{opacity: 0; transform: translateY(30px);}}
        to {{opacity: 1; transform: translateY(0);}}
    }}
    </style>

    <div class="slide">
        <h1>{slide['title']}</h1>
        <img src="{slide['image']}" width="100%" style="border-radius:20px; margin-top:15px;">
        <p style="font-size:24px; margin-top:20px;">{slide['text']}</p>
    </div>
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
    if st.button("Next ➡️"):
        st.session_state.slide += 1
        st.rerun()

# ---------------- FIREWORKS END ----------------
if st.session_state.slide >= len(slides):
    st.balloons()
    st.markdown(
        """
        <h1 style="text-align:center;">🎆 THANK YOU FOR EVERYTHING 🎆</h1>
        <h3 style="text-align:center;">I love you, endlessly 💖</h3>
        """,
        unsafe_allow_html=True
    )