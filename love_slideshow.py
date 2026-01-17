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
PASSWORD = "Onyet0708"   # 🔒 CHANGE THIS

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
# SLIDES CONTENT (EDIT THIS)
# -------------------------------------------------
slides = [
    {
        "title": "💖 Haliuuu my baby onyettt sayang",
        "text": "This is something special, made only for you.",
        "image": "https://drive.google.com/uc?id=1cz2tGTenAW1AiXJrPf1NnYBEUdpjPhTK"
    },
    {
        "title": "🌸 A Gentle Reminder",
        "text": "You are appreciated more than you will ever know.",
        "image": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee"
    },
    {
        "title": "✨ No Matter What",
        "text": "Distance, time, or silence — my heart always finds you.",
        "image": "https://images.unsplash.com/photo-1506744038136-46273834b3fb"
    },
    {
        "title": "💞 Always You",
        "text": "If life lets me choose again, I will still choose you.",
        "image": "https://images.unsplash.com/photo-1526045612212-70caf35c14df"
    }
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
else:
    st.balloons()
    st.markdown(
        """
        <h1 style="text-align:center;">🎆 THANK YOU FOR EVERYTHING 🎆</h1>
        <h3 style="text-align:center;">I love you, endlessly 💖</h3>
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
