import streamlit as st
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
port_stem = PorterStemmer()
vectorization = TfidfVectorizer()

vector_form = pickle.load(open('vector.pkl', 'rb'))
load_model = pickle.load(open('model.pkl', 'rb'))

def stemming(content):
    # Remove non-alphabetic characters and convert to lowercase
    content = re.sub('[^a-zA-Z ]', '', content)
    content = content.lower()
    words = content.split()
    # Stem the words and remove stopwords
    stemmed_words = [port_stem.stem(word) for word in words if word not in stopwords.words('english')]
    return ' '.join(stemmed_words)

def fake_news(news):
    news = stemming(news)  # Preprocess the input text with the stemming function
    input_data = [news]  # Wrap in a list as the model expects an array-like input
    vector_form1 = vector_form.transform(input_data)  # Transform input data to TF-IDF vector
    prediction = load_model.predict(vector_form1)  # Make prediction using the loaded model
    return prediction



if __name__ == '__main__':
    st.title('Fake News Classification app ')
    st.subheader("Input the News content below")
    sentence = st.text_area("Enter your news content here", "",height=200)
    predict_btt = st.button("predict")
    if predict_btt:
        prediction_class=fake_news(sentence)
        print(prediction_class)
        if prediction_class == [0]:
            st.success('Reliable')
        if prediction_class == [1]:
            st.warning('Unreliable')