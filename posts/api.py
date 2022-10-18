"""The API of the posts package"""
from collections import Counter

import matplotlib.pyplot as plt
import numpy as np

from .prepare import read_post_time_data
from .publishing import date_time_to_time
from .publishing import find_posts_between


def most_common_time():
    """Returns the most common time at which users publish their posts.

    :arg
    posts - a pandas dataframe containing the times at which users post.

    :returns
    the most common publishing post time found in the posts dataframe
    """
    all_times = []

    for posts in read_post_time_data('data/instagram_posts.csv', nrows=4000000, chunksize=10000):
        all_times.extend(posts.post_time.tolist())

    most_common_datetime = Counter(all_times).most_common(1)
    most_common_datetime = most_common_datetime[0][0]
    return date_time_to_time(most_common_datetime)


def plot_posts_intervals(intervals):
    """Returns a plot with the number of posts for each given interval.

    :arg
    intervals - a list of tuples where each tuple contains the start and end time (start, end).

    :return
    a plot
    """
    interval_labels = list(map(lambda start_end: f"{start_end[0]} - {start_end[1]}", intervals))
    number_of_posts = np.empty(len(intervals))

    for posts in read_post_time_data('data/instagram_posts.csv'):
        values = find_posts_between(posts, intervals)
        number_of_posts = np.add(number_of_posts, values)

    return plt.barh(interval_labels, number_of_posts)

