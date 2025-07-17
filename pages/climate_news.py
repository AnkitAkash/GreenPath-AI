import streamlit as st
import requests
from utils.chatbot import summarize_article  # Import the summarization function
import os
from dotenv import load_dotenv

# Function to fetch news using NewsAPI
def fetch_news(query="climate change", language="en", page_size=5):
    """Fetch news articles using NewsAPI."""
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/everything?q={query}&language={language}&pageSize={page_size}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json().get("articles", [])
    else:
        st.error(f"Error fetching news: {response.status_code}")
        return []

# Streamlit App
def main():
    st.set_page_config(page_title="🌍 Climate News", page_icon="📰")

    # Custom Styling for Readability
    st.markdown(
        """
        <style>
            .stApp {
                background-color: #E9F5E1;  /* Light green background */
            }
            h1, h2, h3, h4, h5, h6, p, label {
                color: black !important;  /* Ensure all text remains black */
            }
            .news-card {
                background-color: white;
                padding: 15px;
                border-radius: 10px;
                margin-bottom: 15px;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            }
            .news-title {
                font-size: 18px;
                font-weight: bold;
                color: #2E8B57;
            }
            .summary {
                font-size: 16px;
                color: #555;
                white-space: pre-line;  /* Ensure bullet points are displayed correctly */
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("📰 Climate Change News")
    st.write("Stay updated with the latest climate change news, summarized using AI for easy reading.")

    # Fetch news articles
    articles = fetch_news()
    
    if not articles:
        st.error("⚠️ No climate news articles found. Try again later.")
    else:
        for article in articles:
            title = article.get("title", "No Title")
            url = article.get("url", "#")
            description = article.get("description", "No Description Available")

            # Summarize the article
            summary = summarize_article(url)

            # Skip articles with bad summaries
            if "⚠️ Unable to extract" in summary or len(summary) < 20:
                continue

            # Display the article in a card
            st.markdown(f"""
                <div class="news-card">
                    <p class="news-title">{title}</p>
                    <p class="summary">{summary}</p>
                    <a href="{url}" target="_blank">Read Full Article</a>
                </div>
            """, unsafe_allow_html=True)

# Run the Streamlit app
if __name__ == "__main__":
    main()