import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import datetime

def seasonal_plotter(a10, series_name):
    """
    Takes in single time series pandas DF with a single series_name
    
    Usage Instrunctions: 
    """
    
    df = a10.copy()
    df.reset_index(inplace=True)
    df['Year'] = [d.year for d in df.Date]
    df['month'] = [d.strftime('%b') for d in df.Date]
    years = df['Year'].unique()
    years_count = len(years)

    cmap = mpl.cm.winter
    norm = mpl.colors.Normalize(vmin=0, vmax=years_count)

    fig, ax = plt.subplots(figsize=(16, 8), dpi=80)
    
    def seasonal_plotter_single(ax, counter):

        #get year
        the_year = years[counter] 

        #get monthly data for year
        to_plot = df.query('Year == @the_year').filter(['month',series_name]) 

        #plot line
        ax.plot(to_plot['month'], to_plot[series_name], color=cmap(norm(counter))) 

        #add text at end
        ax.text(df.loc[df.Year==years[3], :].shape[0]-0.95, # always a constant
            df.loc[df.Year==years[counter], series_name][-1:].values[0], # last value of the year
            years[counter], color=cmap(norm(counter)), fontsize=10) 

        #add text at start
        ax.text(df.loc[df.Year==years[3], :].shape[0]-12.4,
            df.loc[df.Year==years[counter], series_name][0:1].values[0],
            years[counter], color=cmap(norm(counter)), fontsize=10) 

        return ax
    
    

    # show all complete
    for i in range(1, years_count-1): 
        seasonal_plotter_single(ax, i)

    # for printing the first series
    # seasonal_plotter(ax,0, special=True)

    #for printing last series
    # seasonal_plotter(ax,years_count-1, special=True)

    ax.set_title("Seasonal Plot of Drug Sales Time Series", fontsize=20)
    plt.gca().set(xlim=(-0.5, 11.5), ylim=(2, 30), ylabel='Drug Sales$', xlabel='Month')
    # plt.yticks(fontsize=12, alpha=.7)
    plt.show()