

sentences = [
"I love this product!",
# clearly positive
"This is the worst experience I've ever had.", # clearly negative
"It's okay, not bad but not great.",
# mild positive/neutral
"Absolutely fantastic service!",
# strongly positive
"I'm never buying from here again!"
# strongly negative
]


# from textblob import TextBlob

# print("Sentiment Analysis using TextBlob:\n")
# for sentence in sentences:
#     blob = TextBlob(sentence)
#     sentiment = blob.sentiment.polarity
#     if sentiment > 0:
#         sentiment_label = "Positive"
#     elif sentiment < 0:
#         sentiment_label = "Negative"
#     else:
#         sentiment_label = "Neutral"
#     #output result
#     print(f"Sentence: {sentence}\nSentiment: {sentiment_label} (Polarity: {sentiment})\n")
    
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

print("Sentiment Analysis using VADER:\n")

for sentence in sentences:
    scores = analyzer.polarity_scores(sentence)
    compound = scores['compound']
    if compound >= 0.05:
        sentiment_label = "Positive"
    elif compound <= -0.05:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"
    #output result
    print(f"Sentence: {sentence}\nSentiment: {sentiment_label} (Compound Score: {compound})\n")



#Visualization of sentiment scores
import matplotlib.pyplot as plt
labels =["Positive", "Negative", "Neutral"]
sizes = [3,0,2] #manually counted from above results
colors = ['#66b3ff','#ff6666','#99ff99']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Sentiment Analysis Results")
plt.show()
