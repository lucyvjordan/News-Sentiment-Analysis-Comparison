import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import numpy as np


def DisplayAggregates(aggregateScores):

    websites = list(aggregateScores.keys())
    # get a list of all the websites for x axis
    avgScores = list(x['compound'] for x in aggregateScores.values())
    # get a list of all the average scores
    
    fig, ax = plt.subplots()

    fig.patch.set_facecolor('#f2f2f2')
    ax.set_facecolor('#f2f2f2')
    # changing background colour of inner and outer area of figure
        
    ax.set_axisbelow(True)
    ax.yaxis.grid()
    # creates grid lines

    cmap = mpl.cm.get_cmap('RdYlGn')
    norm = plt.Normalize(min(avgScores), max(avgScores))
    bar_colors = cmap(norm(avgScores))

    ax.bar(websites, avgScores, color = bar_colors, edgecolor = "black", linewidth = 0.3)
    # bar chart of websites plotted against average scores

    ax.set_xticklabels(websites, rotation = 'vertical')
    # sets and rotates x labels so they do not overlap

    ax.set_ylabel("Sentiment", fontsize = 14)
    ax.set_title("Website Analysis", loc = "left", fontsize = 20, pad = 20)

    plt.tight_layout()
    plt.show()



def DisplayAll(aggregateScores):
    
    websites = list(aggregateScores.keys())
    # get a list of all the websites for x axis
    avgScores = np.array(list(x['compound'] for x in aggregateScores.values()))
    # get a list of all the average scores
    negScores = np.array(list(x['neg'] * x['compound'] for x in aggregateScores.values()))
    neuScores = np.array(list(x['neu'] * x['compound'] for x in aggregateScores.values()))
    posScores = np.array(list(x['pos'] * x['compound'] for x in aggregateScores.values()))
    # get lists of all 3 different sentiment scores, in proportion to overall compound sentiment

    fig, ax = plt.subplots()

    fig.patch.set_facecolor('#f2f2f2')
    ax.set_facecolor('#f2f2f2')
    # changing background colour of inner and outer area of figure
    
    ax.set_axisbelow(True)
    ax.yaxis.grid()
    # creates grid lines

    ax.bar(websites, negScores, color = "#ff4d4d", edgecolor = "black", linewidth = 0.3)
    ax.bar(websites, neuScores, bottom = negScores, color = "#ffffcc", edgecolor = "black", linewidth = 0.3)
    ax.bar(websites, posScores, bottom = negScores + neuScores, color = "#b3ffcc", edgecolor = "black", linewidth = 0.3)
    # bar chart of websites plotted against stacked sentiment scores

    ax.legend(["Negative", "Neutral", "Positive"])
    # a key for colours of bars

    ax.set_xticklabels(websites, rotation = 'vertical')
    # sets and rotates x labels so they do not overlap

    ax.set_ylabel("Sentiment", fontsize = 14)
    ax.set_title("Website Analysis", loc = "left", fontsize = 20, pad = 10)
    
    plt.tight_layout()
    plt.show()
