import streamlit as st

st.title("Description of Different Streamlit Application")


st.header('😊Simple Sentiment Analyzer App')
st.image("./images/analyze.jpg")

with st.expander('Sentiment Analyzer'):
    st.markdown("""
    
    #
A sentiment analyzer is a sophisticated tool that employs natural language processing to determine the emotional tone of text, classifying it as positive, negative, or neutral. 
By analyzing factors such as word choice, context, and even emojis, these algorithms provide accurate insights into sentiment across various domains like social media, customer feedback, and market trends.
They are essential for businesses in managing brand reputation, understanding consumer sentiment, and making informed decisions based on data-driven insights. 
Despite challenges with nuances like sarcasm and cultural context, ongoing research improves their accuracy and ethical implementation, ensuring responsible use in analyzing and interpreting textual sentiment in diverse applications.
    """, unsafe_allow_html=True)

st.header('𓍢ִ໋🐱͙֒ Image Classification')
st.image("./images/catbreed.jpg")

with st.expander("Cat Breed Image Classification Project"):
    st.markdown("""
    
    #
    Image classification is a pivotal task in computer vision where algorithms categorize images into predefined classes based on their visual content. 
    Using deep learning models such as convolutional neural networks (CNNs), image classification systems extract hierarchical features from images to recognize patterns and make predictions. 
    These models undergo extensive training on labeled datasets to learn to differentiate between classes like objects, scenes, or patterns. Image classification finds widespread application in fields like autonomous vehicles, medical diagnostics, and quality control in manufacturing, where accurate identification and categorization of visual data are crucial for decision-making and automation. 
    Ongoing advancements in model architectures and training techniques continually enhance the accuracy and efficiency of image classification systems, enabling their integration into diverse real-world applications.     
    """, unsafe_allow_html=True)

st.header('🔮Prediction')
st.image("./images/prediction.png")

with st.expander("Prediction "):
    st.markdown("""
    
    #
This project aims to predict the Filipino Family Income and Expenditure by analyzing historical data from various sources. 
By leveraging quantitative methods and machine learning algorithms, we will identify patterns and key factors that influence household income levels. 
The dataset includes features such as Total Household Income, Total Number of Family members, Household Head Age, and Household Head Sex. 
Our goal is to build a predictive model that accurately forecasts future household incomes for different demographics and regions in the Philippines.
    """, unsafe_allow_html=True)