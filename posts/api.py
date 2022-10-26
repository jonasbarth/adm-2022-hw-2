"""The API of the posts package"""
from collections import Counter

import matplotlib.pyplot as plt
import pandas as pd

from .publishing import find_number_of_posts_between


def most_common_times(posts : pd.DataFrame):
    """Returns the most common time at which users publish their posts.

    :arg
    posts - a pandas dataframe containing the times at which users post.

    :returns
    times, counts - a tuple containing the times normalised to 1970:01:01, and the frequency during that time.
    """
    count_hours = Counter(posts.cts.dt.hour)

    times = list(map(lambda value: pd.Timestamp(1970, 1, 1, value, 0, 0), count_hours.keys()))
    post_frequency = list(count_hours.values())

    return times, post_frequency


def plot_posts_intervals(posts: pd.DataFrame, intervals):
    """Returns a plot with the number of posts for each given interval.

    :arg
    intervals - a list of tuples where each tuple contains the start and end time (start, end).

    :return
    a plot where the intervals are sorted in ascending order and the respective number of posts in that interval.
    """
    intervals.sort()
    interval_labels = list(map(lambda start_end: f"{start_end[0]} - {start_end[1]}", intervals))
    number_of_posts = find_number_of_posts_between(posts, intervals)

    interval_labels.reverse()
    number_of_posts.reverse()
    return plt.barh(interval_labels, number_of_posts)


def timedelta_to_days_minutes(timedelta):
    """Converts a timedelta to days and minutes.

    :args
    timestamp - a pandas timestamp

    :returns
    (days, minutes) - a tuple containing the days and minutes of the timedelta
    """

    minutes = timedelta.components[1] * 60 + timedelta.components[2]

    return timedelta.days, minutes

