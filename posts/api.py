"""The API of the posts package"""
from collections import Counter
from enum import Enum
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np

from .prepare import read_post_time_data
from .publishing import find_number_of_posts_between


class TimePrecision(Enum):
    """Enum for specifying the time precision."""
    SECOND = 0
    MINUTE = 1
    HOUR = 2


def most_common_times(posts : pd.DataFrame, precision : TimePrecision):
    """Returns the most common time at which users publish their posts.

    :arg
    posts - a pandas dataframe containing the times at which users post.

    :returns
    the most common publishing post time found in the posts dataframe
    """
    all_times = []
    if precision == TimePrecision.SECOND:
        all_times = posts.post_time.tolist()

    if precision == TimePrecision.MINUTE:
        posts.post_time = posts.post_time.values.astype('<M8[m]')
        all_times = posts.post_time.tolist()

    if precision == TimePrecision.HOUR:
        posts.post_time = posts.post_time.dt.floor('h')
        all_times = posts.post_time.tolist()

    most_common_datetime = dict(sorted(Counter(all_times).items()))
    labels = list(most_common_datetime.keys())
    values = list(most_common_datetime.values())
    return labels, values


def plot_posts_intervals(posts: pd.DataFrame, intervals):
    """Returns a plot with the number of posts for each given interval.

    :arg
    intervals - a list of tuples where each tuple contains the start and end time (start, end).

    :return
    a plot
    """
    interval_labels = list(map(lambda start_end: f"{start_end[0]} - {start_end[1]}", intervals))
    number_of_posts = np.empty(len(intervals))

    for posts in read_post_time_data('data/instagram_posts.csv', chunksize=10000):
        values = find_number_of_posts_between(posts, intervals)
        number_of_posts = np.add(number_of_posts, values)

    return plt.barh(interval_labels, number_of_posts)

