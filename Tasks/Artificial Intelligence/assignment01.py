# Importing all required libraries
import nltk
import pandas as pd
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# Download essential NLTK datasets
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')


# Creating a few sample product reviews
reviews = [
    "The phone quality is amazing and battery backup is excellent!",
    "Worst product ever. Completely disappointed with this purchase.",
    "It's okay, not bad but not great.",
    "Absolutely fantastic sound quality, I loved it!",
    "I'm never buying from this seller again!",
    "The delivery was quick and packaging was good.",
    "Camera quality is poor and the system lags a lot.",
    "Value for money product, works smoothly.",
    "Very bad experience, received a defective item.",
    "Build quality is strong and looks premium."
]

# Creating DataFrame
df = pd.DataFrame(reviews, columns=["Review"])
print(df)
# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to get sentiment label
def get_sentiment_label(text):
    score = analyzer.polarity_scores(text)['compound']
    if score >= 0.05:
        return 'Positive'
    elif score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Apply sentiment analysis
df['Sentiment'] = df['Review'].apply(get_sentiment_label)
print(df)

# Count sentiment distribution
sentiment_counts = df['Sentiment'].value_counts()
print(sentiment_counts)

# Plot pie chart
labels = sentiment_counts.index
sizes = sentiment_counts.values
colors = ['#66b3ff','#ff6666','#99ff99']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("Sentiment Distribution of Reviews")
plt.axis('equal')
plt.show()


# Example review text
text = "The phone quality is amazing and battery backup is excellent!"

# Step 1: Tokenization
tokens = word_tokenize(text)
print("Tokens:", tokens)

# Step 2: Remove Stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
print("\nFiltered Tokens (No Stopwords):", filtered_tokens)

# Step 3: Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_tokens]
print("\nLemmatized Words:", lemmatized_words)

# Step 4: POS Tagging
pos_tags = nltk.pos_tag(tokens)
print("\nPOS Tags:", pos_tags)


# Real-time sentiment input
# print("\n--- Real-time Sentiment Analysis ---\n")
# while True:
#     user_input = input("Enter your review (or type 'exit' to quit): ")
#     if user_input.lower() == 'exit':
#         break
#     score = analyzer.polarity_scores(user_input)['compound']
#     if score >= 0.05:
#         label = "Positive"
#     elif score <= -0.05:
#         label = "Negative"
#     else:
#         label = "Neutral"
#     print(f"Predicted Sentiment: {label} (Score: {score})\n")

