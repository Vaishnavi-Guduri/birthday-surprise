import streamlit as st
from datetime import datetime
import urllib.parse

# ---------------- SETTINGS ----------------
BESTIE_NAME = "Varuuu"
SECRET_PASSWORD = "vaishu"
BIRTHDAY_DATE = datetime(2026, 1, 30)

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Happy Birthday 💖",
    page_icon="🎂",
    layout="centered"
)

# ---------------- STYLES ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(to bottom, #ffe6f0, #fff5f9);
}
.heart {
    position: fixed;
    color: #ff5c8a;
    animation: float 6s infinite;
    font-size: 24px;
}
@keyframes float {
    0% { bottom: -10%; opacity: 0; }
    50% { opacity: 1; }
    100% { bottom: 110%; opacity: 0; }
}
</style>
""", unsafe_allow_html=True)

# Floating hearts
for i in range(12):
    st.markdown(
        f"<div class='heart' style='left:{i*8+5}%; animation-delay:{i}s'>♥</div>",
        unsafe_allow_html=True
    )

# ---------------- PASSWORD ----------------
st.title("🔒 Private Birthday Surprise")
pwd = st.text_input("Enter the secret password", type="password")

if pwd != SECRET_PASSWORD:
    st.warning("Wrong password 🤭")
    st.stop()

# ---------------- MAIN CONTENT ----------------
st.markdown(f"## 🎉 Happy Birthday {BESTIE_NAME} 🎉")
st.markdown("### Made with love, just for you 💗")

# ---------------- PHOTO UPLOAD ----------------
st.markdown("### 📸 Upload Your Photo")
photo = st.file_uploader("Choose a photo", type=["jpg", "jpeg", "png"])

if photo:
    st.image(photo, caption="My favorite smile 💕", width=300)

# ---------------- MESSAGE ----------------
st.markdown("""
💖 From silly fights to endless laughs,  
💖 From secrets to dreams,  
💖 You are not just my best friend — you are family.

No matter where life takes us,  
I promise this bond stays forever 🤍
""")

# ---------------- FINAL SURPRISE ----------------
if st.button("🎁 Final Surprise"):
    st.balloons()

    st.markdown("## 🌸 A Message From My Heart 🌸")
    st.markdown("""
    You make my life brighter just by being in it.  
    Thank you for choosing me, trusting me,  
    and loving me in your own way.

    **I am always with you — today, tomorrow, forever.**
    """)

    # -------- QR CODE (NO EXTRA LIBRARY) --------
    qr_text = "No matter what happens, you will always be my best friend 🤍"
    encoded = urllib.parse.quote(qr_text)
    qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={encoded}"

    st.image(qr_url, caption="Scan this 💗")

    st.markdown("## 💕 I LOVE YOU MY BEST FRIEND 💕")
    st.markdown("### 🎂 HAPPY BIRTHDAY VARUUU 🎂")

