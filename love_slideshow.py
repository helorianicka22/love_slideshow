import streamlit as st
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="For Onyett Sayang 💖",
    page_icon="💖",
    layout="centered"
)

# ---------------- PASSWORD LOCK ----------------
PASSWORD = "mylove123"   # 🔒 change if you want

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

# ---------------- SLIDES (YOUR EXACT SENTENCES) ----------------
slides = [
    {
        "text": """Haliuuu my baby Onyett Sayanggg 🤍  
Ku buat coding ini special utkmu  
Sbb ku bosan terkurung dlm bilik heheh  

Here we goooo""",
        "symbol": "💖",
        "color": "#ff4d6d"
    },
    {
        "text": """A Gentle Reminder  

Onyett sayang are appreciated & loved by me  
more than you will ever know.""",
        "symbol": "💞",
        "color": "#ff85a1"
    },
    {
        "text": """No matter what nyettt nyettt,  
Distance, time, pain or silence —  
my heart always finds you.""",
        "symbol": "🤍",
        "color": "#f1f1f1"
    },
    {
        "text": """Onyett sayang is very admirable.  
Onyett yg paling rajin, bertanggungjawab,  
pintar, baik  

Mmmuuuaaahhh""",
        "symbol": "🫶",
        "color": "#ff6f91"
    },
    {
        "text": """Di dalam kesusahan onyett,  
kalau ku dekat ku akan datang & bantu.  
Kalau ku jauh, ku akan bantu dari segi  
moral support & DOA""",
        "symbol": "💗",
        "color": "#ff9aa2"
    },
    {
        "text": """Kalau org lain asyik tinggalkanmu,  
Ku di sini akan selalu dgnmu  
(Dari hati terdalam)""",
        "symbol": "🤝❤️",
        "color": "#ffb703"
    },
    {
        "text": """Always onyett sayanggg.  

If life lets me choose again,  
I will still choose you.  
Till death do us part.  

Semangat dalam STUDY WEEK, onyettt kuuu!!!""",
        "symbol": "💓",
        "color": "#e63946"
    }
]

# ---------------- STATE ----------------
if "slide" not in st.session_state:
    st.session_state.slide = 0

last_slide_index = len(slides) - 1

# ---------------- CSS ----------------
st.markdown(
    """
    <style>
    .slide-box {
        text-align: center;
        padding: 60px 40px;
        animation: fadeIn 0.6s ease-in;
        white-space: pre-line;
    }

    .slide-text {
        font-size: 24px;
        line-height: 1.6;
        margin-bottom: 20px;
    }

    .love-symbol {
        font-size: 42px;
        margin-top: 10px;
    }

    .the-end {
        margin-top: 40px;
        font-size: 32px;
        font-weight: bold;
        color: #ff4d6d;
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

# ---------------- THE END + FIREWORKS ----------------
if st.session_state.slide == last_slide_index:
    st.markdown(
        "<div class='the-end' style='text-align:center;'>THE END 💖</div>",
        unsafe_allow_html=True
    )
    st.balloons()

# ---------------- NAVIGATION ----------------
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.session_state.slide > 0:
        if st.button("⬅️ Previous"):
            st.session_state.slide -= 1
            st.rerun()

with col3:
    if st.session_state.slide < last_slide_index:
        if st.button("Next ➡️"):
            st.session_state.slide += 1
            st.rerun()

# ---------------- FOOTER ----------------
st.markdown(
    "<p style='text-align:center; color:grey;'>Made with ❤️, sincerely</p>",
    unsafe_allow_html=True
)
