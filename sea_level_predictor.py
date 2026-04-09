import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    xcol = 'Year'
    ycol = 'CSIRO Adjusted Sea Level'

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x=df[xcol], y=df[ycol])

    # Create first line of best fit
    xrange = np.arange(df[xcol].min(), 2051)
    reg1 = linregress(df[xcol], df[ycol])
    ax.plot(xrange, reg1.intercept + reg1.slope * xrange)

    # Create second line of best fit
    df2 = df[ df[xcol] >= 2000 ]
    reg2 = linregress(df2[xcol], df2[ycol])
    xrange2 = np.arange(df2[xcol].min(), 2051)
    ax.plot(xrange2, reg2.intercept + reg2.slope * xrange2)

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    fig.savefig('sea_level_plot.png')
    return plt.gca()
