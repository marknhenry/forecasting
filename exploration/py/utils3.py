import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import datetime

def seasonal_plotter(a10, series_name, filename, period):
    """
    Takes in single time series pandas DF with a single series_name
    
    Usage Instrunctions: 
    """
    
    df = a10.copy()
    df.index.names = ['Date']
    df.reset_index(inplace=True)

    min_y = df[series_name].min()
    max_y = df[series_name].max()
    min_y = min_y-(max_y-min_y)*0.05
    max_y = max_y+(max_y-min_y)*0.05

    fig, ax = plt.subplots(figsize=(16, 8), dpi=80)

    if (period.lower() == 'year'):
        df['period_col'] = [d.year for d in df.Date]
        df['period_col_child'] = [d.strftime('%b') for d in df.Date]
        periods = df['period_col'].unique()
        periods_count = len(periods)
        min_x = -0.5 # 12 months in a year
        max_x = 11.5
        x_units = 'Month'
    
    if (period.lower() == 'day'):
        df['period_col'] = [d.strftime('%Y-%m-%d') for d in df.Date]  # day
        df['period_col_child'] = [d.strftime('%H') for d in df.Date]  # hour
        periods = df['period_col'].unique()
        periods_count = len(periods)
        min_x = -0.5 # 24 hours in a day
        max_x = 23.5
        x_units = 'Hour'
    
    if (period.lower() == 'week'):
        df['period_col'] = [d.strftime('%Y-%U') for d in df.Date]  # week
        df['period_col_child'] = df.Date
        periods = df['period_col'].unique()
        periods_count = len(periods)
        min_x = -0.5 # 7 days in a week, but looking hourly
        max_x = (24*7)-.5
        x_units = 'Day'

    cmap = mpl.cm.winter
    norm = mpl.colors.Normalize(vmin=0, vmax=periods_count)
    
    def seasonal_plotter_single(ax, counter, add_text=False):

        #get period
        the_period = periods[counter] 

        #get child period for period
        to_plot = df.query('period_col == @the_period').filter(['period_col_child',series_name]) 

        if (period.lower() == 'week'):
            # to_plot['TempDate'] = pd.date_range("2012-01-01", periods=to_plot.shape[0], freq="H")
            to_plot['counter'] = range(len(to_plot))
            ax.plot(to_plot['counter'], to_plot[series_name], color=cmap(norm(i)), linewidth=1) 
        else:
            #plot line
            ax.plot(to_plot['period_col_child'], to_plot[series_name], color=cmap(norm(counter)), linewidth=1) 

        if add_text: 
            #add text at end
            ax.text(df.loc[df['period_col']==periods[1], :].shape[0]-0.95, # always a constant
                df.loc[df['period_col']==periods[counter], series_name][-1:].values[0], # last value of the year
                periods[counter], color=cmap(norm(counter)), fontsize=10) 

            #add text at start
            ax.text(df.loc[df['period_col']==periods[1], :].shape[0]-12.4,
                df.loc[df['period_col']==periods[counter], series_name][0:1].values[0],
                periods[counter], color=cmap(norm(counter)), fontsize=10) 

        return ax
    
    for i in range(1, periods_count-1): # show all except first and last
        seasonal_plotter_single(ax, i)

    seasonal_plotter_single(ax,0) # for printing the first series

    seasonal_plotter_single(ax,periods_count-1) #for printing last series

    ax.set_title('{} per {}'.format(series_name, x_units), fontsize=20)
    plt.gca().set(xlim=(min_x, max_x), ylim=(min_y, max_y), ylabel=series_name, xlabel=x_units)
    if (period=='week'):
        x_ticks=[]
        week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        for i in range(7):
            for j in range(12): 
                x_ticks.append(' ')
            x_ticks.append(week_days.pop(0))
            for j in range(11): 
                x_ticks.append(' ')
        plt.xticks(range(168) , x_ticks)
        ax.xaxis.set_ticks_position('none') 
    plt.savefig(filename)
    plt.show()
    