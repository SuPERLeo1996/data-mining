import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font = FontProperties(fname='C:\\Windows\\Fsimsun.ttc', size=16)

if __name__ == '__main__':
    df = pd.read_csv('pandas.csv')
    sorted_df = df.sort_values(by='month', ascending=False)

    # grouped_month = sorted_df["unit"].groupby(sorted_df["month"])
    # grouped_month.mean().plot(kind='bar')
    # plt.show()

    grouped_location_month = sorted_df["unit"].groupby([sorted_df["location1"], sorted_df["month"]])
    print(grouped_location_month.mean())
    grouped_location_month.mean().plot()
    plt.show()
