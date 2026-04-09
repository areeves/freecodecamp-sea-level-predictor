import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    year_col=df['Year']
    csiro_col=df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x=year_col, y=csiro_col)

    # Create first line of best fit
    year_range = np.arange(year_col.min(), 2051)
    reg1 = linregress(year_col, csiro_col)
    ax.plot(year_range, reg1.intercept + reg1.slope * year_range)


    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
