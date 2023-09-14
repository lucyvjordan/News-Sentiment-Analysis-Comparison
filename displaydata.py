import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import numpy as np


class Display():
    def __init__(self, aggregateScores):

        self.currentToggle = False

        self.websites = list(aggregateScores.keys())
        # get a list of all the websites for x axism 
        self.avgScores = np.array(list(x['compound'] for x in aggregateScores.values()))
        # get a list of all the average scores
        self.negScores = np.array(list(x['neg'] * x['compound'] for x in aggregateScores.values()))
        self.neuScores = np.array(list(x['neu'] * x['compound'] for x in aggregateScores.values()))
        self.posScores = np.array(list(x['pos'] * x['compound'] for x in aggregateScores.values()))
        # get lists of all 3 different sentiment scores, in proportion to overall compound sentiment

        self.fig, self.ax = plt.subplots()
        
        self.rax = plt.axes([0.63, 0.88, 0.35, 0.1])
        # axes of toggle button

    def Update(self):
        self.ax.clear()
        self.rax.clear()
        # clear all axes (so when toggle it doesnt repeatedly draw over previous elements)

        self.fig.patch.set_facecolor('#ecf2f9')
        self.ax.set_facecolor('#f2f2f2')
        # changing background colour of inner and outer area of figure
        
        self.ax.set_axisbelow(True)
        self.ax.yaxis.grid()
        # creates grid lines behind bar chart

        self.ax.set_ylabel("Sentiment", fontsize = 14)
        self.ax.set_title("News Sentiment", loc = "left", fontsize = 25, pad = 20)
        
        toggleButton = Button(self.rax, "Show Breakdown of Scores", color = 'white')
        toggleButton.on_clicked(self.Toggle)
        # button to toggle graph, directs program to self.Toggle() function when clicked

        if self.currentToggle == False:
            self.DisplayAggregates()
        else:
            self.DisplayAll()

        self.ax.set_xticks(self.ax.get_xticks())
        self.ax.set_xticklabels(self.websites, rotation = 'vertical')
        # sets and rotates x labels so they do not overlap   
            
        plt.tight_layout()
        # fits the chart onto screen
        plt.show()


    def DisplayAggregates(self):

        cmap = mpl.cm.get_cmap('RdYlGn')
        # retrieving colour map of Red-Yellow-Green
        norm = plt.Normalize(min(self.avgScores), max(self.avgScores))
        # scales data to a range of 0 - 1
        bar_colors = cmap(norm(self.avgScores))
        # creates list of colours for each bar of bar chart

        self.ax.bar(self.websites, self.avgScores, color = bar_colors, edgecolor = "black", linewidth = 0.3)
        # bar chart of websites plotted against average scores


    def DisplayAll(self):
    
        self.ax.bar(self.websites, self.negScores, color = "#ff4d4d", edgecolor = "black", linewidth = 0.3)
        self.ax.bar(self.websites, self.neuScores, bottom = self.negScores, color = "#ffffcc", edgecolor = "black", linewidth = 0.3)
        self.ax.bar(self.websites, self.posScores, bottom = self.negScores + self.neuScores, color = "#b3ffcc", edgecolor = "black", linewidth = 0.3)
        # bar chart of websites plotted against stacked sentiment scores

        self.ax.legend(["Negative", "Neutral", "Positive"], loc = "lower left")
        # a key for the colours of the bars


    def Toggle(self, event):

        self.currentToggle = not self.currentToggle
        # sets to True if False, and vice versa

        self.Update()

