# For tokenization
# For stopwords
# For Lemmatization

import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk. download('averaged_perceptron_tagger') # For POS tagging

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

text = "Natural Language Processing with Python is very interesting and useful for building AI applications."

import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk. download('averaged_perceptron_tagger') # For POS tagging

# Step 1: Install & Import
import nltk
nltk.download('punkt')
nltk.download('all')

from nltk.tokenize import word_tokenize

# Step 2: Text input
text = "Natural Language Processing is fun and educational."

# Step 3: Tokenization
tokens = word_tokenize(text)
print("Tokens:", tokens)

# Download the tokenizer data

stop_words = set(stopwords.words('english'))

filtered_tokens = [word for word in tokens if word. lower() not in stop_words]
print("Filtered Tokens (No Stopwords):", filtered_tokens)

lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer. lemmatize(word) for word in filtered_tokens]
print("Lemmatized Words:", lemmatized_words)


pos_tags = nltk. pos_tag(tokens)
print("POS Tags:", pos_tags)
# Tag Meaning (examples):

# NN: Noun

# JJ: Adjective

# VBZ: Verb (3rd person)

# RB: Adverb
