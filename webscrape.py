import requests
from bs4 import BeautifulSoup

import analysis
from displaydata import Display

websites = {"BBC": "www.bbc.co.uk/news", 
            "The Guardian": "www.theguardian.com/uk",
            "Sky News": "news.sky.com",
            "The Telegraph": "www.telegraph.co.uk/news/",
            "Mail Online": "www.dailymail.co.uk/news/index.html",
            "Independent": "www.independent.co.uk/",
            "Positive.News": "www.positive.news/",
            "The Sunday Times": "www.thetimes.co.uk/",
            "Metro": "metro.co.uk/news/uk/"}


''' to do:
https://www.thesun.co.uk/news/uknews/
https://thegoodnewshub.com/
https://www.mirror.co.uk/news/uk-news/
https://www.msn.com/en-gb/news/uk
'''

def scrape_headlines(websites):

    allScores = []
    aggregateScores = {}

    for x in websites:

        websiteURL = "https://" + websites[x]
        # creates URL for web request using values in dictionary
        try:
            website = requests.get(websiteURL, timeout = 1)
            # connects to website, returns exception if not connected within 1 second
        except:
            print(f"Cannot connect to: {x}")
            break
            # prints statement to console displaying which website hasnt been connected to

        soup = BeautifulSoup(website.content, "html.parser")
        # BeautifulSoup module makes extracting data from website easier

        headlines = []

        # news websites are separated because the way to direct the soup to the headlines differs between websites
        # BBC
        if x == "BBC":
            container = soup.find("div", id="news-top-stories-container")
            # identifies div where main stories are

            for headline in container.select('h3[class*="promo-heading__title"]'):
                if headline.get_text() not in headlines:
                    # in case headlines are repeated
                    headlines.append(headline.get_text()) 


        # THE GUARDIAN
        elif x == "The Guardian":
            container = soup.find("div", id="container-headlines")

            for headline in container.find_all('a'):
                try: 
                    headlines.append(headline['aria-label'])
                except:
                    pass # because not a headline text (all headlines texts have aria-labels)


        # SKY NEWS
        elif x == "Sky News":
            container = soup.find("div", class_ = "sdc-site-tiles__group")

            for headline in container.select('span[class="sdc-site-tile__headline-text"]'):
                headlines.append(headline.get_text())

        
        # THE TELEGRAPH
        elif x == "The Telegraph":
            container  = soup.find("ul", class_ = "article-list__list")

            for headline in container.find_all('span', attrs = {'class': ''}):
                # finds all span content with no class (as this contains text of headline - other span content with a class may include 'live', additional information etc)
                headlines.append(headline.get_text())

        # MAIL ONLINE
        elif x == "Mail Online":
            container = soup.find("div", attrs= {'data-track-module': 'sm-403^automated_tabbed_headlines'})

            for headline in container.find_all('li', attrs= {'class': ''}):
                headlines.append(headline.get_text().strip(" \n"))
                # strips text because it usually contains lots of empty space and new lines

        # INDEPENDENT
        elif x == "Independent":

            divisionTypes = ["HeroPlus3Articles", "ArticleX8PlusDMPU"]

            for division in divisionTypes:

                container = soup.find('div', attrs= {'data-type': division})

                for headline in container.find_all('a', attrs = {'class': 'title'}):
                    headlines.append(headline.get_text())
        
        # POSITIVE.NEWS
        elif x == "Positive.News":

            divisionClasses = ["latest__articles cols--3--2--2", "featured__articles cols--3--3--1"]
            
            for division in divisionClasses:

                container = soup.find('div', attrs= {'class': division})

                for headline in container.find_all('a', attrs = {'class': 'card__title h3'}):
                    headlines.append(headline.get_text())

        # THE SUNDAY TIMES
        elif x == "The Sunday Times":

            container = soup.find('div', attrs = {'class': 'SliceCollection'})
            
            for headline in container.select('h3[class*="Item-headline"]'):
                headlines.append(headline.find('a').get_text())

        # METRO
        elif x == "Metro":

            divisionIDs = ["trending-module category colour-neutral", "widget-area channel-middle channel-area sidebar clearfix"]
            
            for division in divisionIDs:

                container = soup.find('div', attrs= {'class': division})

                for headline in container.find_all('h3'):
                    print(headline.get_text())
                    headlines.append(headline.get_text())

                for headline in container.find_all('h2'):
                    print(headline.get_text())
                    headlines.append(headline.get_text())


        # ANALYSIS
        headlineAnalysis = analysis.Analyse(headlines)
        # uses Analyse() function from analysis.py to analyse all of the headlines

        #allScores.append(headlineAnalysis[0])
        # contains positive, neutral, negative and compound
        aggregateScores[x] = headlineAnalysis
        # is the average of all the compound scores of the headlines

    Display(aggregateScores)
      
scrape_headlines(websites)

