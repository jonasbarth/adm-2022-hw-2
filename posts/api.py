"""The API of the posts package"""
from collections import Counter

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
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


def timedelta_to_days_minutes(timedelta):
    """Converts a timedelta to days and minutes.

    :args
    timestamp - a pandas timestamp

    :returns
    (days, minutes) - a tuple containing the days and minutes of the timedelta
    """

    minutes = timedelta.components[1] * 60 + timedelta.components[2]

    return timedelta.days, minutes

