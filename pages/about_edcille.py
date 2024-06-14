import streamlit as st

st.title(" Fun Facts about Edcille Deine T. Telequido 🎉 ")



st.title("Gallery 🧚")


image_paths = ["images\idsil1.jpg", "images\idsil2.jpg", "images\idsil3.jpg"]


cols = st.columns(len(image_paths))

for col, image_path in zip(cols, image_paths):
    col.image(image_path)


st.header("👨‍🎓 TELEQUIDO, EDCILLE DEINE T.")

# st.markdown("""
# ##### 👨‍👦‍👦 Family Members

# * 🤱 **Mother's Name:** Ma. Cecilia T. Telequido
# * 👨 **Father's Name:** Edwin A. Telequido
# * 👦 **Brother's Name:** Ezequiel T. Telequido
# ### 🔎 Overview
# """, unsafe_allow_html=True)

# Personal Information
st.header("✨ Personal Information ✨")
st.write("**Name:** EDCILLE DEINE T. TELEQUIDO 🧚")
st.write("**Date of Birth:** AUGUST 26, 2002 📅")
st.write("**Age:** 21 years old 💜")
st.write("**Education:** Currently studying at CARLOS HILADO MEMORIAL STATE UNIVERSITY 📖")
st.write("**Program:** Bachelor of Science in Information Systems 🖥️")
st.write("**Year:** 3rd year 📚")
st.write("**Location:** PASEO MABINI ST., ZONE 4-A, TALISAY CITY, NEGROS OCCIDENTAL 🏡")


with st.expander("My Vision for the Future: A 10-Year Forecast"):
    st.markdown("""
    
    #
    ### 💫 Ten Years From Now: A Journey of Resilience and Success 💫
    
            After ten years, my IS degree has not only helped me get a career 
            developing safe automated systems, 
            but it has also given me the skills I need to survive in a world where technology 
            and people are becoming increasingly linked.

    #### 🌠 Personal Growth and Vision 🌠

           After ten years, the late hours spent studying have paid off. 
           Using my IS degree, I lead a bright team in a state-of-the-art software company, 
           creating solutions that transform people's lives.  
           Most importantly, even with the most demanding deadlines, my ability to solve problems, 
           which I developed in college, allows me to remain composed.

    #### 🎇 Dreams and Aspirations 🎇

           In ten years, I envision myself at the edge of innovation, heading up a group of developers 
           that create the next generation of safe, efficient platforms that change how people use technology. 
           Since then, I have also been wanting to be an aspirant who undertakes psychology as a second degree.
    """, unsafe_allow_html=True)

# Quotes
st.header("Favorite Quotes")
st.write(" *\"Real knowledge is to know the extent of one's ignorance.\"* - Confucius")
st.write(" *\"Knowledge without experience is useless.\"* - Plato")
st.write(" *\"I dwell in possibility.\"* - Emily Dickinson")
st.write(" *\"There is nothing like staying at home for real comfort.\"* - Jane Austen")


import streamlit as st


images = [
    {"path": "./images/3b1.jpg", "caption": "Couldn't have coded my way through these past few years without the late-night study sessions, shared caffeine jitters, and endless support from my amazing classmates! ☕️"},
    {"path": "./images/3b2.jpg", "caption": "They're more than just classmates, they're my chosen family, forever bonded by all-nighters, coding triumphs, and the occasional existential crisis. "},
    {"path": "./images/3b3.jpg", "caption": "Here's to friendships forged in firewalls and fueled by coffee!"}
]


st.title("🖼️Gallery")


for image in images:
    st.image(image["path"], caption=image["caption"])



st.markdown(
    """
    <style>
    .stApp {
        background-color: black; /* Light grey background */
        padding: 2em;
        font-family: "Times New Roman", sans-serif; /* Elegant font */
    }
    h1, h2 {
        color: #734F96; /* Lavender color for headings */
    }
    .stText {
        font-size: 1.2em;
        color: #333; /* Dark text color */
    }
</style>

    """,
    unsafe_allow_html=True
)


st.write("### Thanks for getting to know me by visiting my profile 😊")
