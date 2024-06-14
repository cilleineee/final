import streamlit as st
st.set_page_config(layout="wide", page_title="Learnings")

st.title("WHAT I HAVE LEARNED")

st.image("images/ML.jpg")

st.markdown("""
#
                LEARNINGS FROM ITEQMT COURSE: 
The third year of IS has shown me that information systems are as much about building bridges between people and technology as they are about coding. 
It's about understanding how technology can empower individuals and organizations to achieve their goals efficiently. This field has deepened my appreciation for the synergy between innovation and practical application, 
highlighting the transformative potential of well-designed systems.""", unsafe_allow_html=True)

with st.expander("LEARNINGS FROM APPLICATION PROJECTS💭"):
    st.markdown("""
    #
        Image Classification:
            This image classification project helped me learn more about how to teach computers to "see" 
            and classify the environment.

        Sentiment Analysis:
            Building my sentiment analyzer project this year proved that data 
            can reveal the hidden language of emotions.
                
        Prediction of Data Sets:
            This data sets project showed me the power of turning raw information into 
            insights, making me even more excited about the possibilities of information systems. 
    """, unsafe_allow_html=True)
