import streamlit as st
import nltk
from nltk.classify import NaiveBayesClassifier
from nltk.probability import FreqDist
import pickle
import matplotlib.pyplot as plt
import seaborn as sns


# Define features (words) and their corresponding labels (positive/negative)
def word_features(words):
    return {word: True for word in words}

# Define training data for different emotions
happy_words = ['happy', 'enthusiastic', 'glad', 'elated', 'pleased']
sad_words = ['sad', 'unhappy', 'melancholy', 'gloomy', 'sorrowful']
angry_words = ['angry', 'enraged', 'furious', 'wrathful', 'irritated']
excited_words = ['excited', 'thrilled', 'eager', 'overjoyed', 'fired up']
nervous_words = ['nervous', 'anxious', 'uneasy', 'agitated', 'tense']
scared_words = ['scared', 'frightened', 'afraid', 'spooked', 'alarmed']

happy_features = [(word_features(word.split()), 'happy') for word in happy_words]
sad_features = [(word_features(word.split()), 'sad') for word in sad_words]
angry_features = [(word_features(word.split()), 'angry') for word in angry_words]
excited_features = [(word_features(word.split()), 'excited') for word in excited_words]
nervous_features = [(word_features(word.split()), 'nervous') for word in nervous_words]
scared_features = [(word_features(word.split()), 'scared') for word in scared_words]

# Combine features for different emotions
train_set = happy_features + sad_features + angry_features + excited_features + nervous_features + scared_features

# Train the Naive Bayes classifier
classifier = NaiveBayesClassifier.train(train_set)

# Save the trained classifier to a pickle file
with open('pages/emotion_classifier.pkl', 'wb') as f:
    pickle.dump(classifier, f)

# Define emotion emojis
emojis = {
    'happy': '😊',
    'sad': '😢',
    'angry': '😡',
    'excited': '😃',
    'nervous': '😰',
    'scared': '😱'
}

# Streamlit application setup
st.set_page_config(
    page_title="Emotion Analysis",
    page_icon="😊",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.title("Emotion Analysis")

user_input = st.text_area("Enter text for emotion analysis", "")

if st.button("Analyze"):
    if user_input:
        # Load the classifier from the pickle file
        with open('pages\emotion_classifier.pkl', 'rb') as f:
            loaded_classifier = pickle.load(f)

        # Classify the input text
        features = word_features(user_input.split())
        sentiment = loaded_classifier.classify(features)
        prob_dist = loaded_classifier.prob_classify(features)
        probabilities = {label: prob_dist.prob(label) for label in prob_dist.samples()}

        # Display results
        st.write(f"Emotion: {sentiment} {emojis[sentiment]}")
        st.write(f"Probabilities: {probabilities}")

        # Display probability scores in a bar chart
        labels = list(probabilities.keys())
        scores = list(probabilities.values())

        fig, ax = plt.subplots()
        sns.barplot(x=scores, y=labels, palette="viridis", ax=ax)
        ax.set_title("Emotion Probabilities")
        ax.set_xlabel("Probability")
        ax.set_ylabel("Emotion")
        st.pyplot(fig)

        # Display confidence level
        confidence = max(probabilities.values())
        st.write(f"Confidence: {confidence:.2f}")

    else:
        st.write("Please enter some text for analysis.")
