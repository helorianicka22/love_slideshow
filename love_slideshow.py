import streamlit as st
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="For Onyett Sayang 💖",
    page_icon="💖",
    layout="centered"
)

# ---------------- PASSWORD LOCK ----------------
PASSWORD = "mylove123"

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

# ---------------- SLIDES WITH SHAPES ----------------
slides = [
    {
        "text": """Haliuuu my baby Onyett Sayanggg 🤍
Ku buat coding ini special utkmu
Sbb ku bosan terkurung dlm bilik heheh

Here we goooo""",
        "symbol": "💖",
        "shape": "trapezium",
        "color": "#ffd6e0"
    },
    {
        "text": """A Gentle Reminder

Onyett sayang are appreciated & loved by me
more than you will ever know.""",
        "symbol": "💞",
        "shape": "circle",
        "color": "#ffe5ec"
    },
    {
        "text": """No matter what nyettt nyettt,
Distance, time, pain or silence —
my heart always finds you.""",
        "symbol": "🤍",
        "shape": "speech",
        "color": "#f1f1f1"
    },
    {
        "text": """Onyett sayang is very admirable.
Onyett yg paling rajin, bertanggungjawab,
pintar, baik

Mmmuuuaaahhh""",
        "symbol": "🫶",
        "shape": "soft-heart",
        "color": "#ffccd5"
    },
    {
        "text": """Di dalam kesusahan onyett,
kalau ku dekat ku akan datang & bantu.
Kalau ku jauh, ku akan bantu dari segi
moral support & DOA""",
        "symbol": "💗",
        "shape": "diamond",
        "color": "#ffe0b2"
    },
    {
        "text": """Kalau org lain asyik tinggalkanmu,
Ku di sini akan selalu dgnmu
(Dari hati terdalam)""",
        "symbol": "🤝❤️",
        "shape": "note",
        "color": "#e0f7fa"
    },
    {
        "text": """Always onyett sayanggg.

If life lets me choose again,
I will still choose you.
Till death do us part.

Semangat dalam STUDY WEEK, sayang!!!""",
        "symbol": "💓",
        "shape": "final",
        "color": "#ffb3c1"
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
    .box {
        padding: 50px;
        margin: auto;
        max-width: 600px;
        text-align: center;
        font-size: 23px;
        line-height: 1.6;
        white-space: pre-line;
        animation: fadeIn 0.6s ease-in;
    }

    .rounded { border-radius: 25px; }
    .circle { border-radius: 50%; padding: 80px; }
    .speech { border-radius: 20px; position: relative; }
    .soft-heart { border-radius: 40px 40px 60px 60px; }
    .diamond { transform: rotate(45deg); }
    .diamond span { display: inline-block; transform: rotate(-45deg); }
    .note { border-radius: 10px; box-shadow: 5px 5px 0 #ccc; }
    .final { border-radius: 30px; border: 3px dashed #ff4d6d; }

    .love {
        font-size: 42px;
        margin-top: 20px;
    }

    .the-end {
        margin-top: 40px;
        font-size: 32px;
        font-weight: bold;
        color: #ff4d6d;
        text-align: center;
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

if slide["shape"] == "diamond":
    content = f"<span>{slide['text']}</span>"
else:
    content = slide["text"]

st.markdown(
    f"""
    <div class="box {slide['shape']}" style="background:{slide['color']};">
        {content}
        <div class="love">{slide['symbol']}</div>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------- THE END + FIREWORKS ----------------
if st.session_state.slide == last_slide_index:
    st.markdown("<div class='the-end'>THE END 💖</div>", unsafe_allow_html=True)
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
    "<p style='text-align:center; color:grey;'>Made with ❤️, just for you</p>",
    unsafe_allow_html=True
)

