import streamlit as st
from datetime import datetime, timedelta

# ---------------- SETTINGS ----------------
BESTIE_NAME = "Varuuu"
SECRET_PASSWORD = "vaishu"
BIRTHDAY_DATE = datetime(2026, 1, 30)
# -----------------------------------------

st.set_page_config(
    page_title="Happy Birthday 💖",
    page_icon="🎂",
    layout="centered"
)

# ---------------- STYLES (LIGHT PINK + HEART ANIMATION) ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(to bottom, #ffe6f0, #fff5f9);
}

/* Floating hearts */
.heart {
    position: fixed;
    width: 16px;
    height: 16px;
    background: #ff6f91;
    transform: rotate(45deg);
    animation: floatUp 10s linear infinite;
    opacity: 0.5;
}

.heart::before,
.heart::after {
    content: "";
    width: 16px;
    height: 16px;
    background: #ff6f91;
    border-radius: 50%;
    position: absolute;
}

.heart::before { top: -8px; left: 0; }
.heart::after { left: -8px; top: 0; }

@keyframes floatUp {
    0% { bottom: -10%; opacity: 0; }
    50% { opacity: 0.6; }
    100% { bottom: 110%; opacity: 0; }
}
</style>

<div class="heart" style="left:10%;"></div>
<div class="heart" style="left:25%;"></div>
<div class="heart" style="left:40%;"></div>
<div class="heart" style="left:55%;"></div>
<div class="heart" style="left:70%;"></div>
<div class="heart" style="left:85%;"></div>
""", unsafe_allow_html=True)

# ---------------- PASSWORD ----------------
st.title("🔐 Private Birthday Surprise")
password = st.text_input("Enter the secret password", type="password")

if password != SECRET_PASSWORD:
    st.warning("This surprise is only for someone very special 🤍")
    st.stop()

# ---------------- MAIN TITLE ----------------
st.markdown(
    f"<h1 style='text-align:center;color:#e64980;'>Happy Birthday {BESTIE_NAME}</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='text-align:center;color:#d6336c;'>Made with love, just for you</h3>",
    unsafe_allow_html=True
)

st.write("---")

# ---------------- IMAGE UPLOAD ----------------
st.subheader("📸 A Photo That Means a Lot")

uploaded_image = st.file_uploader(
    "Click here → select the photo → Open",
    type=["jpg", "jpeg", "png"]
)

if uploaded_image is not None:
    st.image(uploaded_image, use_container_width=True)

st.write("---")

# ---------------- COUNTDOWN ----------------
now = datetime.now()
midnight = BIRTHDAY_DATE + timedelta(days=1)

if now < midnight:
    remaining = midnight - now
    h, r = divmod(remaining.seconds, 3600)
    m, s = divmod(r, 60)

    st.info(
        f"Time left for your birthday day to end: "
        f"{remaining.days} days {h} hours {m} minutes {s} seconds"
    )
else:
    st.success("Your birthday day may end, but you remain special forever 💖")

st.write("---")

# ---------------- MESSAGE ----------------
st.subheader("💌 A Message From My Heart")

st.write(f"""
Hey {BESTIE_NAME},

Some people enter our lives quietly  
and slowly become everything.

You are my comfort on difficult days,  
my laughter without reason,  
and my constant without conditions.
""")

st.write("---")

st.subheader("💭 Something I Wanted You to Know")

st.write("""
I know sometimes my words hurt you, and for that I’m truly sorry.  
Please believe me — if my words hurt, my heart never does.

I trust you a lot, and deep inside I believe you’ll never leave me.

When I get angry, words come out that I don’t really mean,  
and I know you may not always understand me in those moments.  
That hurts me too.

Sometimes I feel like I’m not your first priority,  
and that’s the part that hurts the most.

I just wish you would value my words  
and listen to me the way I listen to you.

No matter what, I care about you more than I can explain,  
and I hope you know that my feelings come  
from a place of trust and attachment — not anger.
""")

st.write("---")

# ---------------- SURPRISE ----------------
if st.button("🎁 Open Your Surprise"):
    st.balloons()
    st.success("This bond is forever 🌸")

st.write("---")

# ---------------- FINAL HEARTFUL ENDING ----------------
st.subheader("🤍 From My Heart, Always")

st.write("""
No matter how life changes,  
no matter how busy days become,  
there will always be a part of my heart  
that feels safe because of you.

You matter to me more than you realize —  
not because of what you do,  
but because of who you are.

Thank you for being you,  
for your patience, your presence,  
and for staying, even when things aren’t easy.

I’m grateful for you — today and always.
""")

st.write("---")

st.markdown(
    "<h1 style='text-align:center;color:#e64980;'>Happy Birthday Varuuu 🎂💗</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='text-align:center;color:#d6336c;'>I LOVE YOU, MY BEST FRIEND 🤍</h3>",
    unsafe_allow_html=True
)
