import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()


def Analyse(headlines):

    sentimentScores = {'neg': 0, 'neu': 0, 'pos': 0, 'compound': 0}

    for line in headlines:
        scores = analyzer.polarity_scores(line)
        # analyse the headline using vader

        sentimentScores['neg'] += scores['neg']
        sentimentScores['neu'] += scores['neu']
        sentimentScores['pos'] += scores['pos']
        sentimentScores['compound'] += scores['compound']
        # increase total negative, neutral, positive and compound (average) scores
    
    for key in sentimentScores.keys():
        # for each category (negative/neutral/positive/compound)
        sentimentScores[key] = round(sentimentScores[key] / len(headlines), 3)
        # find the average by dividing by number of headlines

    return sentimentScores
