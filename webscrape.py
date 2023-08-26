import requests
from bs4 import BeautifulSoup

# BBC

newswebsite = "https://www.bbc.co.uk/news"
website = requests.get(newswebsite)
soup = BeautifulSoup(website.content, "html.parser")

container = soup.find("div", id="latest-stories-tab-container")
# id = "news-top-stories-container" -- for only top stories

bbctitles = []
for title in container.select('h3[class*="promo-heading__title"]'):
    if title.get_text() not in bbctitles:
        bbctitles.append(title.get_text()) 
print(bbctitles)
