import feedparser
import requests
from transformers import pipeline   #performing sentiment analysis on text

# Initialize sentiment analysis pipeline
pipe = pipeline('sentiment-analysis')

api_key = 'cuj2oo9r01qm7p9n68lgcuj2oo9r01qm7p9n68m0'
ticker = 'META'
keyword = 'meta'

# Get stock data for Meta Platforms (META) from Finnhub API
# Formulate the API URL to fetch real-time stock data
stock_api_url = f'https://finnhub.io/api/v1/quote?symbol={ticker}&token={api_key}'
response = requests.get(stock_api_url)


if response.status_code == 200:
    #if successful, parse JSON response and extract stock data
    data = response.json()
    #printing stock data
    print("Stock Data for META:\n")
    print(f"Current Price: {data['c']}\n")
    print(f"High Price of the day: {data['h']}\n")
    print(f"Low Price of the day: {data['l']}\n")
    print(f"Open Price of the day: {data['o']}\n")
    print(f"Previous Close Price: {data['pc']}\n")
else:
    print(f"Error fetching data: {response.status_code}")

# Fetch the RSS feed for news articles related to the keyword 'META'
rss_feed_url = "https://news.google.com/rss/search?q=META&hl=en-US&gl=US&ceid=US:en"
response = requests.get(rss_feed_url)

# Parse the RSS feed using feedparser
feed = feedparser.parse(response.text)
    
total_score = 0
num_articles = 0

for entry in feed.entries:
    #printing article title, link, date, and summary
    print(f'Title: {entry.title}\n')
    print(f'Link: {entry.link}\n')
    print(f'Published: {entry.published}\n')
    print(f'Summary: {entry.summary}\n')

    #performance of sentiment analysis on article summary
    sentiment = pipe(entry.summary)[0]

    # Print the sentiment label (Positive, Negative, or Neutral) and the score
    print(f'Sentiment {sentiment["label"]}, Score: {sentiment["score"]}')
    print('-' * 40)

    if sentiment['label'] == 'POSITIVE':
        total_score += sentiment['score']
    elif sentiment['label'] == 'NEGATIVE':
        total_score -= sentiment['score']
        num_articles += 1   # Count the number of articles with negative sentiment

#Calculate and print the overall sentiment based on the average score
if num_articles > 0:
    final_score = total_score / num_articles
    print(f'Overall Sentiment: {"Positive" if final_score >= 0.15 else "Negative" if final_score <= -0.15 else "Neutral"} {final_score}')
else:
    print("No articles matched the keyword.")