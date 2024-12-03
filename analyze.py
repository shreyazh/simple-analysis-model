from textblob import TextBlob
import time
import random
def tweet_stream():
    tweets = ["I love this product! It's amazing.",
        "Worst experience ever, will not buy again!",
        "This product is decent, but not worth the price.",
        "Absolutely fantastic service, will recommend!",
        "I hate this product, very disappointing!"]
    while True:
        yield random.choice(tweets)
        time.sleep(1)
def analyze_sentiment(stream):
    for tweet in stream:
        sentiment = TextBlob(tweet).sentiment.polarity
        if sentiment > 0:
            sentiment_label = "Positive"
        elif sentiment < 0:
            sentiment_label = "Negative"
        else:
            sentiment_label = "Neutral"
        print(f"Tweet: {tweet} | Sentiment: {sentiment_label}")
        break
tweet_data = tweet_stream()
analyze_sentiment(tweet_data)
