import requests
from bs4 import BeautifulSoup

import analysis
from displaydata import Display

websites = {"BBC": "www.bbc.co.uk/news", 
            "The Guardian": "www.theguardian.com/uk",
            "Sky News": "news.sky.com",
            "The Telegraph": "telegraph.co.uk/news/",
            "Mail Online": "dailymail.co.uk/news/index.html"}


def scrape_headlines(websites):

    allScores = []
    aggregateScores = {}

    for x in websites:

        websiteURL = "https://" + websites[x]
        # creates URL for web request using values in dictionary

        website = requests.get(websiteURL)
        # connects to website

        soup = BeautifulSoup(website.content, "html.parser")
        # BeautifulSoup module makes extracting data from website easier

        # news websites are separated because the way to direct the soup to the headlines differs between websites
        # BBC
        if x == "BBC":
            
            container = soup.find("div", id="news-top-stories-container")
            # identifies div where main stories are

            headlines = []
            for headline in container.select('h3[class*="promo-heading__title"]'):
                if headline.get_text() not in headlines:
                    # in case headlines are repeated
                    headlines.append(headline.get_text()) 


        # THE GUARDIAN
        elif x == "The Guardian":
            container = soup.find("div", id="container-headlines")

            headlines = []

            for headline in container.find_all('a'):
                try: 
                    headlines.append(headline['aria-label'])
                except:
                    pass # because not a headline text (all headlines texts have aria-labels)


        # SKY NEWS
        elif x == "Sky News":
            container = soup.find("div", class_ = "sdc-site-tiles__group")

            headlines = []

            for headline in container.select('span[class="sdc-site-tile__headline-text"]'):
                headlines.append(headline.get_text())

        
        # THE TELEGRAPH
        elif x == "The Telegraph":
            container  = soup.find("ul", class_ = "article-list__list")

            headlines = []

            for headline in container.find_all('span', attrs = {'class': ''}):
                # finds all span content with no class (as this contains text of headline - other span content with a class may include 'live', additional information etc)
                headlines.append(headline.get_text())

        elif x == "Mail Online":
            container = soup.find("div", attrs= {'data-track-module': 'sm-403^automated_tabbed_headlines'})

            headlines = []

            for headline in container.find_all('li', attrs= {'class': ''}):
                headlines.append(headline.get_text().strip(" \n"))
                # strips text because it usually contains lots of empty space and new lines

        # ANALYSIS
        headlineAnalysis = analysis.Analyse(headlines)
        # uses Analyse() function from analysis.py to analyse all of the headlines

        #allScores.append(headlineAnalysis[0])
        # contains positive, neutral, negative and compound
        aggregateScores[x] = headlineAnalysis
        # is the average of all the compound scores of the headlines

    Display(allScores, aggregateScores)
      
scrape_headlines(websites)

