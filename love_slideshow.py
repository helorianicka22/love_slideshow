import streamlit as st
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="For Someone Special 💖",
    page_icon="💖",
    layout="centered"
)

# ---------------- PASSWORD LOCK ----------------
PASSWORD = "mylove123"   # 🔒 change this if you want

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

# ---------------- SLIDES CONTENT (7 SLIDES) ----------------
slides = [
    {
        "text": "💖 Haliuuu my baby onyett sayang",
        "symbol": "❤️",
        "color": "#ff4d6d"
    },
    {
        "text": "You are the first thought in my morning and the last in my night.",
        "symbol": "💞",
        "color": "#ff85a1"
    },
    {
        "text": "No matter how far life takes us, my heart always knows where to return.",
        "symbol": "🤍",
        "color": "#f1f1f1"
    },
    {
        "text": "Holding your hand feels like holding the whole world.",
        "symbol": "🫶",
        "color": "#ff6f91"
    },
    {
        "text": "You make ordinary days feel extraordinary.",
        "symbol": "💗",
        "color": "#ff9aa2"
    },
    {
        "text": "If love had a shape, it would look like us.",
        "symbol": "🤝❤️",
        "color": "#ffb703"
    },
    {
        "text": "I love you — quietly, deeply, endlessly.",
        "symbol": "💓",
        "color": "#e63946"
    }
]

# ---------------- STATE ----------------
if "slide" not in st.session_state:
    st.session_state.slide = 0

# ---------------- CSS ----------------
st.markdown(
    """
    <style>
    .slide-box {
        text-align: center;
        padding: 60px 30px;
        animation: fadeIn 0.6s ease-in;
    }

    .slide-text {
        font-size: 26px;
        margin-bottom: 20px;
    }

    .love-symbol {
        font-size: 42px;
        margin-top: 10px;
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
    slide = slides[st.session_state.slide]

    st.markdown(
        f"""
        <div class="slide-box">
            <div class="slide-text">{slide['text']}</div>
            <div class="love-symbol" style="color:{slide['color']};">
                {slide['symbol']}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.balloons()
    st.markdown(
        """
        <h1 style="text-align:center;">💖 THE END 💖</h1>
        <h3 style="text-align:center;">Thank you for being my love.</h3>
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
