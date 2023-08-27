import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

def Analyze(headlines):

    sentimentScores = []
    
    for line in headlines:
        scores = analyzer.polarity_scores(line)
        sentimentScores.append(scores)
    
    return sentimentScores
