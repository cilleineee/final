import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

add_page_title()
show_pages(
    [   
        Page("homepage.py", "ITEQMT Machine Learning Application Portfolio", "🤖"),
        Section("HOMEPAGE", "🌐"),
        Page("pages/about_edcille.py", "ABOUT EDCILLE", "🧚", in_section=True),
        Page("pages/app_desc.py", "APP DESCRIPTION", "⌨️", in_section=True),
        Page("pages/learnings.py", "WHAT I'VE LEARNED", "💡", in_section=True),
    
  
        Section("PROJECTS", "🛠️"),
        Page("pages/prediction_dataset.py", "PREDICTION", "🔮", in_section=True),
        Page("pages/sentiment_analyzer.py", "SENTIMENT ANALYZER", "📊", in_section=True),
        Page("pages/image_class.py", "IMAGE CLASSIFICATION", "🖼️", in_section=True),


         Section("SOURCE CODES", "🔒"),
        Page("pages/prediction_dataset_src.py", "PREDICTION", "📡", in_section=True),
        Page("pages/sentiment_analyzer_src.py", "SENTIMENT ANALYZER", "📡", in_section=True),
        Page("pages/image_class_src.py", "IMAGE CLASSIFICATION", "📡", in_section=True),
    

    ]
)

hide_pages(["Thank you"])

st.markdown("### ITEQMT ENDTERM - FINAL REQUIREMENTS CREATED BY: ")
st.header("TELEQUIDO, EDCILLE DEINE T. - BSIS 3B")
st.image("images/deine.jpg")
st.markdown("""<a href="/photographer/thinkstock-83786">Thinkstock</a> on <a href="/">Freeimages.com</a>""",unsafe_allow_html=True,)

st.info("For more info. Contact [Edcille Deine](https://www.facebook.com/cilleine) on Fb")
st.info("┆ Please take note when on streamlit.app the [Image Classification] pages are not working due to Memory Limitation of 'Free Tier' hosting of Streamlit"┆) 
st.markdown("---")

with st.expander("⋮ HISTORY, PURPOSE AND USAGE"):
    st.markdown("""
    
    #
The creation of the first neural networks in the 1950s and 1960s, as well as Alan Turing's fundamental question, "Can machines think?" are credited with helping to establish machine learning, a subset of artificial intelligence, in the middle of the 20th century. 
Its main goal is to make computers capable of learning from data and gradually enhancing their performance without the need for explicit programming. 
The use of machine learning algorithms, which use patterns found in massive datasets to forecast or make judgments, has increased quickly. 
These applications are affecting industries like marketing, banking, healthcare, and autonomous systems. 
With rising computing power and easier access to massive amounts of data, machine learning is being used more and more.
""", unsafe_allow_html=True)

st.markdown("""
### ᯓ INTRODUCTION ᯓ""", unsafe_allow_html=True)


st.image("images/p1.jpg")


st.markdown("""
            
Introducing our new platform, Streamlit Application Project: an interactive web interface that showcases data science's capabilities. 
The goal of this project is to demonstrate how data science approaches may be used in practice to solve real-world issues. Three main areas are our focus: 
            data-driven decision making, predictive modeling, and exploratory data analysis.
### ⚙️ Machine Learning Techniques


##### ☰ More Info

   USAGE AND EXAMPLES OF MACHINE LEARNING
            
Machine learning is widely used across various domains to enhance decision-making, automate processes, and gain insights from data. 
In healthcare, it enables predictive analytics for disease diagnosis and personalized treatment plans. 
In finance, algorithms detect fraudulent transactions and manage investment portfolios. 
Retailers use machine learning for personalized marketing and inventory management. 
Autonomous vehicles rely on machine learning for navigation and obstacle detection. 
Additionally, natural language processing applications, such as chatbots and translation services, improve customer interactions. 
These examples illustrate how machine learning transforms industries by leveraging data to solve complex problems and optimize performance.


### ⭐ Star the project on Github  <iframe src="https://ghbtns.com/github-btn.html?user=koalatech&repo=streamlit_web_app&type=star&count=true"  width="150" height="20" title="GitHub"></iframe>   
""", unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
