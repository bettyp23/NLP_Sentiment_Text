# AI-Powered Sentiment Analysis and Stock Data Script

This script utilizes **Artificial Intelligence (AI)** to perform **sentiment analysis** on news articles related to **Meta Platforms (META)** while also fetching **real-time stock data** for a comprehensive analysis. By leveraging **HuggingFace's transformers library** for sentiment classification and the **Finnhub API** for stock data, this script demonstrates how AI can be used to gain insights from text data and real-time market trends.

## How AI is Involved

This script heavily relies on **AI and Natural Language Processing (NLP)** techniques to analyze and classify the sentiment of news articles. The key AI components are:

### Sentiment Analysis (NLP/AI):
- The **HuggingFace Transformers** library is used to load a **pre-trained sentiment analysis model** powered by deep learning techniques.
- This model, typically based on transformer architectures like **BERT** or **DistilBERT**, has been trained on vast datasets to **understand** the **context**, **nuances**, and **relationships** between words in text, making it ideal for **text classification** tasks such as sentiment analysis.
- The AI model predicts whether the sentiment of each article's summary is **positive**, **negative**, or **neutral**, providing an intuitive way to gauge public perception about Meta Platforms.

### AI Sentiment Classification:
- For each news article, the AI model classifies the sentiment based on its summary. It uses its trained knowledge to detect the tone of the text, outputting a sentiment label (positive, negative, or neutral) along with a **sentiment score** indicating the strength of that sentiment.
- This sentiment analysis is a direct application of **AI** to understand human language, making the process of analyzing large volumes of text much more efficient and accurate compared to manual methods.

### Transformer Models:
- The script uses **transformer-based models**, which are state-of-the-art for natural language tasks. These models, such as **BERT** and **DistilBERT**, excel at capturing relationships between words and context, allowing them to make highly accurate predictions on the sentiment of text data.
- The use of these **pre-trained models** significantly reduces the time and computational power required for training custom models, making it easier to implement AI for sentiment analysis.

## Overview of the Script

### Imports:
- **feedparser**: Parses RSS feeds to extract news article data.
- **requests**: Handles HTTP requests to fetch stock data and the RSS feed.
- **transformers (pipeline)**: Loads and uses a pre-trained sentiment analysis model from HuggingFace.

### Fetching Stock Data:
- The script fetches **real-time stock data** for **Meta Platforms (META)** using the **Finnhub API**. The data includes key stock metrics such as **current price**, **high**, **low**, **open**, and **previous close**.
- The stock data is printed if the API request is successful, giving you a snapshot of the company's market performance.

### Fetching News Feed:
- The script fetches an **RSS feed** from **Google News** for articles related to Meta Platforms. The feed contains information like the article **title**, **link**, **publication date**, and **summary**.

### Sentiment Analysis of News Articles:
- Each article's **summary** is processed by the AI-powered sentiment analysis model. The model assigns a **sentiment label** (positive, negative, or neutral) and a **sentiment score** to each summary.
- This allows you to quickly determine the sentiment of a large number of news articles without manually reading each one.

### Final Sentiment Calculation:
- After processing all articles, the script calculates the **average sentiment score** for articles with negative sentiment. It then classifies the overall sentiment of the news feed as **positive**, **negative**, or **neutral** based on the aggregated score.

### Final Output:
- The script outputs the sentiment classification and score for each article, as well as an overall sentiment score and classification for the entire news feed. This provides a **comprehensive sentiment analysis** of news related to Meta Platforms (META) in real-time.

---

## Key AI Techniques Used

### 1. **Text Classification with AI**:
   - The sentiment analysis model is an application of **text classification**, which is a core task in **Natural Language Processing (NLP)**. It categorizes the sentiment of each article as positive, negative, or neutral based on its content.

### 2. **Deep Learning and Transformers**:
   - The **transformer-based models** like **BERT** and **DistilBERT** used by the AI are **deep learning models** that have revolutionized NLP by enabling machines to understand language at a deeper level. These models are pre-trained on large text corpora and can be fine-tuned for specific tasks like sentiment analysis.

### 3. **Pre-Trained Models**:
   - The use of **pre-trained transformer models** saves considerable time and resources. Instead of training a model from scratch, the script uses a model that has already learned the intricacies of language through training on vast amounts of text data, allowing for fast and accurate sentiment predictions.

---

## Requirements:
- Python 3.x
- `requests` library: For making API requests to fetch stock data and RSS feeds.
- `feedparser` library: For parsing RSS feeds.
- `transformers` library: For sentiment analysis using a pre-trained model.

You can install the required libraries using the following command:

```bash
pip install requests feedparser transformers