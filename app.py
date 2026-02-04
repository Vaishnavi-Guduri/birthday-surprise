import streamlit as st
from datetime import datetime
import qrcode
from io import BytesIO

# ---------------- SETTINGS ----------------
BESTIE_NAME = "Varuuu"
SECRET_PASSWORD = "vaishu"   # change if you want
# ------------------------------------------

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

h1, h2, h3, p {
    text-align: center;
    font-family: 'Trebuchet MS', sans-serif;
}

.heart {
    position: fixed;
    color: #ff4d6d;
    animation: float 6s infinite ease-in;
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
for i in range(8):
    st.markdown(
        f"<div class='heart' style='left:{i*12+5}%; animation-delay:{i}s;'>❤</div>",
        unsafe_allow_html=True
    )

# ---------------- PASSWORD ----------------
st.markdown("## 🔒 Private Birthday Surprise")

password = st.text_input("Enter the secret password", type="password")

if password != SECRET_PASSWORD:
    st.info("Enter the correct password to unlock 💖")
    st.stop()

# ---------------- MAIN CONTENT ----------------
st.markdown(f"<h1>Happy Birthday {BESTIE_NAME} 🎂💗</h1>", unsafe_allow_html=True)
st.markdown("<h3>Made with love, just for you</h3>", unsafe_allow_html=True)

st.markdown("---")

# ---------------- PHOTO (DIRECT) ----------------
st.markdown("### 💖 A Memory I Love")

st.image(
    "bestie.jpg",     # <-- image file name
    caption="Us 🤍",
    use_container_width=True
)

# ---------------- MESSAGE ----------------
st.markdown("""
<p>
I know sometimes my words hurt you, and for that I’m truly sorry.  
Please believe me—if my words hurt, my heart never does.  
<br><br>
I trust you deeply, and somewhere inside me, I believe you’ll never leave me.  
When I get angry, I say things I don’t really mean, and I know it hurts.  
That hurts me too.
<br><br>
Sometimes I feel like I’m not your first priority, and that’s the part that hurts the most.  
I just wish you would value my words the way I value yours.
<br><br>
No matter what, I care about you more than I can explain.  
My feelings come from trust, attachment, and love — never anger.
</p>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------- QR CODE ----------------
st.markdown("### 📌 One Last Little Surprise")

qr_text = "No matter what happens, you will always be my best friend 🤍"

qr = qrcode.make(qr_text)
buf = BytesIO()
qr.save(buf)
buf.seek(0)

st.image(buf, caption="Scan this 🤍")

st.markdown("---")

# ---------------- FINAL LINES ----------------
st.markdown(
    "<h2 style='color:#e64980;'>Happy Birthday Varuuu 🎉</h2>",
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='color:#d6336c;'>I LOVE YOU, MY BESTEST FRIEND 🤍</h3>",
    unsafe_allow_html=True
)
