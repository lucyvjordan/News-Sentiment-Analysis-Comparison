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


# The Guardian

newswebsite = "https://www.theguardian.com/uk"

website = requests.get(newswebsite)

soup = BeautifulSoup(website.content, "html.parser")

container = soup.find("div", id="container-headlines")

guardiantitles = []
for title in container.find_all('a'):
    try: 
        guardiantitles.append(title['aria-label']) # check this is working with new headlines tomorrow
    except:
        pass # because not a headline text (all headlines texts have aria-labels)
print(guardiantitles)
