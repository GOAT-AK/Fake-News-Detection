# Fake-News-Detection
Fake News Detection Project using Support Vector Machine (SVM) for Natural Language processing [CS411P] at Faculty of Computers &amp; Information Sciences, Mansoura University

# Table of Content

* [Brief](#Brief)
* [DataSet](#DataSet)
* [How It Works](#HowItWorks)
* [Tools](#Tools)
* [Remarks](#Remarks)
* [Usage](#Usage)
* [Sample Run](#SampleRun)


# Brief

With the proliferation of misinformation online, identifying fake news has become increasingly important. This project aims to develop a reliable tool to classify news articles as fake or real using a Support Vector Machine (SVM) model. By analyzing textual content, the model predicts the reliability of news articles, contributing to the fight against misinformation.


# DataSet

The dataset used in this project is the [Fake News Dataset](https://www.kaggle.com/competitions/fake-news/data?select=train.csv) from Kaggle. This dataset contains various news articles, including features such as the author, title, and content, along with a label indicating whether the news is real (1) or fake (0).  


# How It Works

- The dataset is loaded from a CSV file.
- Missing values in the text data are handled appropriately.
- Text preprocessing is performed, including cleaning, stemming, and removing stopwords.
- Features (text content) and target labels (fake/real) are separated.
- The dataset is split into training and testing sets.
- A TF-IDF Vectorizer is applied to convert text data into numerical format.
- An SVM model is trained on the training data.
- The model predicts the reliability of news articles based on the text content.



# Tools & Libraries

I. Jupyter Notebook & VS Code

II. Python 3.x

III. pandas

IV. re

V. nltk

VI. scikit-learn

VII. pickle

VIII. Streamlit



# Remarks
* This Python program was run and tested in Jupyter Notebook.
* Ensure the required libraries are installed by running:

  ```bash
  pip install pandas nltk scikit-learn streamlit

# Usage

To begin utilizing this application, follow these steps:

1. Clone this repository:
   
   ```bash
   git clone https://github.com/GOAT-AK/Fake-News-Detection

2. Navigate to the cloned repository:

   ```bash
   cd Fake-News-Detection

3. Run the Jupyter Notebook:

   ```bash
   Fake_News_NLP.ipynb

4. Launch the Streamlit app:
   
   ```bash
   streamlit run app.py
    

# Sample Run


* The Content Reliable

![Screenshot 2024-11-05 at 7 06 57 pm](https://github.com/user-attachments/assets/86104ec7-8710-4e6d-ac92-b7188daa7c42)


<hr>


* The Content Unreliable

![Screenshot 2024-11-05 at 7 07 24 pm](https://github.com/user-attachments/assets/dc72517b-44d4-4648-ae54-f95e0a80b0cb)

  
  
