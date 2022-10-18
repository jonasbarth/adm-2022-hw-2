"""Module for handling posts data"""
import pandas as pd
from .publishing import date_time_to_time


def read_post_time_data(path : str, chunksize=1000, nrows=1000):
    """Returns a generator for sanitised post data.

    :arg
    path - the path of the .csv file that will be read. Should be relative to where the code is run from.

    :return
    a generator for a chunk of the overall .csv file.
    """
    for posts in pd.read_csv(path, sep='\t', usecols=['cts'], parse_dates=['cts'], chunksize=chunksize, nrows=nrows):
        posts = sanitise(posts)
        yield posts


def sanitise(posts: pd.DataFrame):
    """Santises the instagram posts dataframe.

    Santising steps:
    - filter out NaN values
    - create a new column where the date will be the same for all rows
    - convert new column to datetime and make the date be the same for all rows

    :arg
    posts - a pandas dataframe containing a cts column.

    :return
    the sanitised pandas dataframe.
    """

    posts = posts[posts.cts.notna()]
    posts["post_time"] = posts.cts.apply(date_time_to_time)
    posts.post_time = pd.to_datetime(posts.post_time, format="%H:%M:%S")

    return posts