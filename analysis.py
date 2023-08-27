import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()


def Analyse(headlines):

    sentimentScores = []
    totalScore = 0

    for line in headlines:
        scores = analyzer.polarity_scores(line)
        sentimentScores.append(scores)
        totalScore += scores['compound']
    
    averageScore = round(totalScore / len(headlines), 3)

    return sentimentScores, averageScore

