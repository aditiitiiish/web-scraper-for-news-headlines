import requests
from bs4 import BeautifulSoup

# Get the webpage content
url = "https://www.bbc.com/news"
page = requests.get(url)

# Use BeautifulSoup to read the HTML
soup = BeautifulSoup(page.text, "html.parser")

# Find all h2 and h3 tags (these usually contain headlines)
headlines = soup.find_all(["h2", "h3"])

# Open a text file to save the headlines
with open("news_headlines.txt", "w", encoding="utf-8") as file:
    for i, tag in enumerate(headlines, 1):
        headline = tag.get_text().strip()
        if len(headline) > 10:  # Skip very short lines
            file.write(f"{i}. {headline}\n")

print("Headlines saved in news_headlines.txt")
