import matplotlib as mpl
import matplotlib.pyplot as plt

def Display(aggregateScores):
    
    websites = list(aggregateScores.keys())
    # get a list of all the websites for x axis
    avgScores = list(x['compound'] for x in aggregateScores.values())
    # get a list of all the average scores

    plt.bar(websites, avgScores)
    # bar chart of websites plotted against average scores

    plt.show()