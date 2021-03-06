import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import datetime


def seasonal_plotter(a10, series_name, period, filename='result.jpg', include_text=False):
    """
    Takes in single time series pandas DF with a single series_name

    Usage Instrunctions: 
    """

    df = a10.copy() # Work on a copy
    df.index.names = ['Date'] # Unify name of index
    df.reset_index(inplace=True) # to reset it and get a single name

    if(period.lower() == 'year'):
        df['period_col'] = [d.year for d in df.Date]  # year
        df['period_child_col'] = [d.strftime('%b') for d in df.Date]  # month
        period_child_col = 'Month'
        periods = df['period_col'].unique()
        periods_count = len(periods)
        min_x = -0.5
        max_x = 12.5
        min_y = df[series_name].min()
        max_y = df[series_name].max()

    elif(period.lower() == 'day'):
        df['period_col'] = [d.strftime('%Y-%m-%d') for d in df.Date]  # day
        df['period_child_col'] = [d.strftime('%H') for d in df.Date]  # hour
        period_child_col = 'Hour'
        periods = df['period_col'].unique()
        periods_count = len(periods)
        df.to_csv('intermediate.csv')
        min_x = -0.5
        max_x = 24.5
        min_y = df[series_name].min()
        max_y = df[series_name].max()

    cmap = mpl.cm.winter
    norm = mpl.colors.Normalize(vmin=0, vmax=periods_count)

    fig, ax = plt.subplots(figsize=(16, 8), dpi=80)

    def seasonal_plotter_single(ax, counter):

        # get year
        the_period = periods[counter]

        # get monthly data for year
        to_plot = df.query(
            'period_col == @the_period').filter(['period_child_col', series_name])

        # plot line
        ax.plot(to_plot['period_child_col'], to_plot[series_name],
                color=cmap(norm(counter)))

        # if(include_text):
        #     # add text at end
        #     ax.text(df.loc[df.period_col == periods[1], :].shape[0]-0.95,  # always a constant
        #             # last value of the year
        #             df.loc[df.period_col == periods[counter],
        #                 series_name][-1:].values[0],
        #             periods[counter], color=cmap(norm(counter)), fontsize=10)

        #     # add text at start
        #     ax.text(df.loc[df.period_col == periods[1], :].shape[0]-12.4,
        #             df.loc[df.period_col == periods[counter],
        #                 series_name][0:1].values[0],
        #             periods[counter], color=cmap(norm(counter)), fontsize=10)

        return ax

    # show all complete
    for i in range(1, periods_count):
        seasonal_plotter_single(ax, i)
    # seasonal_plotter_single(ax, 2)

    # for printing the first series
    # seasonal_plotter(ax,0, special=True)

    # for printing last series
    # seasonal_plotter(ax,periods_count-1, special=True)

    ax.set_title(filename.split('.')[0], fontsize=20)
    plt.gca().set(xlim=(min_x, max_x), ylim=(min_y, max_y),
                  ylabel=filename.split('.')[0], xlabel=period_child_col)
    # plt.yticks(fontsize=12, alpha=.7)
    plt.show()
    plt.savefig(filename)
