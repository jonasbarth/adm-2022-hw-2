"""Module that contains functions for the times at which users publish their posts"""
import numpy as np
import pandas as pd


def find_number_of_posts_between(posts: pd.DataFrame, intervals):
    """Finds posts with post times within the given list of inclusive intervals.

    :arg
    posts - a pandas dataframe containing the times at which users post.
    intervals - a list of tuples where each tuple contains the start and end time (start, end).

    :return
    intervals - a list of intervals as strings.
    """
    number_of_posts = np.array([_find_number_of_posts_between(posts, start, end) for start, end in intervals])
    return number_of_posts


def _find_number_of_posts_between(posts: pd.DataFrame, start_time, end_time):
    """Finds posts between the given inclusive start and inclusive end interval.

    :arg
    posts - a pandas dataframe containing the times at which users post.
    start_time - a time (hh:MM:ss) for the start of the interval.
    end_time - a time (hh:MM:ss) for the end of the interval.

    :returns
    the number of posts between the given interval
    """
    return len(find_posts_between(posts, start_time, end_time))


def find_posts_between(posts : pd.DataFrame, start_time, end_time):
    """Finds all the instagram posts in the inclusive [start, end] interval.

    :arg
    cols - a list of column names that the dataset should have when read.
    start_time - a time (hh:MM:ss) for the start of the interval.
    end_time - a time (hh:MM:ss) for the end of the interval.

    :returns
    a pandas DataFrame with the posts with columns cts, numbr_likes, number_comments, that are in the interval
    """
    start_time = pd.Timestamp(f"1970-01-01 {start_time}")
    end_time = pd.Timestamp(f"1970-01-01 {end_time}")
    start_time_hour = posts.cts.dt.hour >= start_time.hour
    start_time_minute = posts.cts.dt.minute >= start_time.minute
    start_time_second = posts.cts.dt.second >= start_time.second

    end_time_hour = posts.cts.dt.hour <= end_time.hour
    end_time_minute = posts.cts.dt.minute <= end_time.minute
    end_time_second = posts.cts.dt.second <= end_time.second

    start_time_mask = start_time_hour & start_time_minute & start_time_second
    end_time_mask = end_time_hour & end_time_minute & end_time_second
    interval_mask = start_time_mask & end_time_mask
    posts_in_interval = posts.loc[interval_mask]

    return posts_in_interval
