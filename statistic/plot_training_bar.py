import os
import matplotlib.pyplot as plt
import numpy as np

def addlabels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i]+0.5, y[i], ha='center')


if __name__ == '__main__':
    # creating data on which bar chart will be plot
    x = ["web", "command", "zalo 1", "voice 2", "disabled", "vin", "vlsp 2019", "zalo 2", "voice 1", "self prepare"]
    y = [12.53, 2.50, 19.01, 2.94,  3.89, 13.75, 2.95, 14.62,4.38, 12.21]
    # setting figure size by using figure() function
    plt.figure(figsize=(10, 5))
    # making the bar chart on the data
    plt.bar(x, y, 0.8)
    # calling the function to add value labels
    addlabels(x, y)
    plt.ylim(0,22)
    # giving title to the plot
    # plt.title("College Admission")
    # giving X and Y labels
    plt.xlabel("Dataset")
    plt.ylabel("WER")
    # visualizing the plot
    plt.show()