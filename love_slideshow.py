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
PASSWORD = "Onyettt0708"   # 🔒 CHANGE THIS

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
        "title": "💖 Haliuuu My Baby Onyettt Sayanggg",
        "text": "This is something special, made only for you.",
    },
    {
        "title": "🌸 A Gentle Reminder utk onyettt sayang",
        "text": "During your hard time, ku shelalu akan ada untukmu, more than you will ever know.",
    },
    {
        "title": "✨ No Matter What nyettt nyettt",
        "text": "Distance, time, pain atau silence — my heart always finds onyettt.",
        "text": "Onyettt sayang always the most admirable ones.",
        "text": "Onyettt sayang paling rajin, paling bertanggungjawab, paling pintar, paling baik.",
    },
    {
        "title": "💞 Always Onyettt & only Onyettt",
        "text": "If life lets me choose again, I will still choose onyettt sayanggg. Sihat2 shelalu yaaa~",
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

