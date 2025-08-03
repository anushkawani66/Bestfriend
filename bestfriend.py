import streamlit as st
from PIL import Image
import random

# 🌸 Title and Subtitle
st.title("🌸 For My Loviee Dovieee 🌸")
st.markdown("##### Made with love by Anuuuuu 🧸💌")
st.markdown("Heyyy munchkin!! Here's a special little place just for **you**. 🌈💖")

# 📖 Scrapbook Subtitle
st.subheader("📘 Our Scrapbook Memories")

# 🌼 Set Up Your Image Paths
image_paths = [
    "IMG-20250803-WA0033.jpg",
    "IMG-20250803-WA0034.jpg",
    "IMG-20250803-WA0035.jpg",
    "IMG-20250803-WA0036.jpg",
    "IMG-20250803-WA0037.jpg",
    "IMG-20250803-WA0038.jpg",
    "IMG-20250803-WA0039.jpg",
    "IMG-20250803-WA0040.jpg",
    "IMG-20250803-WA0041.jpg",
    "IMG-20250803-WA0042.jpg"
]

# 🧠 Session state for page navigation
if "page" not in st.session_state:
    st.session_state.page = 0

# ➕ Navigation Buttons
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.button("⬅️ Previous"):
        if st.session_state.page > 0:
            st.session_state.page -= 1

with col3:
    if st.button("Next ➡️"):
        if st.session_state.page < len(image_paths) - 1:
            st.session_state.page += 1

# 🖼️ Display current image
current_page = st.session_state.page
st.markdown(f"### 📄 Page {current_page + 1} of {len(image_paths)}")
image = Image.open(image_paths[current_page])
st.image(image, use_container_width=True, caption=f"💖 Memory Page {current_page + 1}")

# 🎉 Final Message (NO balloons)
if current_page == len(image_paths) - 1:
    st.success("That's the end of our mini scrapbook! 💫💖")

# 💘 Quiz Section
st.subheader("🎲 How Well Do You Know Me? Quiz 🎀")

quiz_data = [
    {
        "question": "What's my favourite colour?",
        "options": ["Pink", "Blue", "Black", "Purple"],
        "correct": "Black"
    },
    {
        "question": "My dream vacation place?",
        "options": ["Switzerland", "Maldives", "Bali", "Paris"],
        "correct": "Paris"
    },
    {
        "question": "What snack do I ALWAYS crave?",
        "options": ["Chocolate", "Pizza", "Ice Cream", "Momos"],
        "correct": "Pizza"
    },
    {
        "question": "Which nickname do you call me the most?",
        "options": ["Anu", "Cutie", "Stupid", "BFF"],
        "correct": "Anu"
    }
]

for i, q in enumerate(quiz_data):
    st.markdown(f"**{q['question']}**")
    user_answer = st.radio("", q["options"], key=f"q{i}")
    if st.button(f"Check answer for: {q['question']}", key=f"btn{i}"):
        if user_answer == q["correct"]:
            st.success("🎉 Woahhh you're right! You really know me 💖")
        else:
            st.error("😢 Oops! That's not it... but it's okay, I still love ya 💞")

st.markdown("🌟 *You're already the best for trying!* 🌟")

# 🎁 Secret Gift Box
st.subheader("🎁 Your Secret Gift Box 🎁")

if st.button("🎀 Open Your Gift", use_container_width=True):
    # No st.balloons()
    st.image("https://c.tenor.com/-GCUaOzv5-AAAAAd/big-hug-for-you-hugs.gif", width=300)
    st.markdown("### 🧸 A Cozy Teddy Hug Just for You 💖")
    messages = [
        "This teddy is sending you the biggest hug ever! 🧸💫",
        "You deserve a fluffy cuddle hug right now 💕",
        "When in doubt, teddy hugs it out! 🤗",
        "This bear told me: you're loved infinitely 🐻🎀",
        "Soft. Sweet. Squishy. That’s your virtual bear hug 💌"
    ]
    st.success(random.choice(messages))

# 💖 Compliment Section
st.subheader("💖 A Little Compliment Just for You 💖")

compliments = [
    "You're made of magic and sunshine 🌞✨",
    "You make the world brighter just by being in it 🌈💗",
    "You're my safe space and sparkle buddy 🌸💫",
    "You're as soft as a marshmallow and twice as sweet 🍬💕",
    "Life's better with you in it — you're my favourite notification 📱💘",
    "You're not just cute... you're ✨legendary cute✨"
]

if st.button("💬 Click here for a surprise compliment!"):
    st.success(random.choice(compliments))

# 💌 Write a message about them
st.subheader("📝 Your Special Note 💌")

default_note = """I hope you liked this small cute surprise ...
I love you my sweetheart 💖
Happy friendship dayyy my babygirl 🧸🌈"""

note = st.text_area("Write something special about them here:", value=default_note, height=150)

if note:
    st.success("💗 Your message has been saved in their heart (and memory too)!")
