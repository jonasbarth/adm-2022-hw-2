"""Module that contains functions for the times at which users publish their posts"""
import pandas as pd
import numpy as np


def date_time_to_time(datetime):
    """Removes the date from the datetime object and returns a time in format HH:MM:SS."""

    datetime = pd.Timestamp(datetime)
    hour = f"{datetime.hour}" if datetime.hour > 9 else f"{0}{datetime.hour}"
    minutes = f"{datetime.minute}" if datetime.minute > 9 else f"{0}{datetime.minute}"
    seconds = f"{datetime.second}" if datetime.second > 9 else f"{0}{datetime.second}"

    return f"{hour}:{minutes}:{seconds}"


def find_posts_between(posts: pd.DataFrame, intervals):
    """Finds posts with post times within the given list of inclusive intervals.

    :arg
    posts - a pandas dataframe containing the times at which users post.
    intervals - a list of tuples where each tuple contains the start and end time (start, end).

    :return
    intervals - a list of intervals as strings.
    """
    number_of_posts = np.array([_find_posts_between(posts, start, end) for start, end in intervals])
    return number_of_posts


def _find_posts_between(posts: pd.DataFrame, start_time, end_time):
    """Finds posts between the given inclusive start and  inclusive end interval.

    :arg
    posts - a pandas dataframe containing the times at which users post.
    start_time - a time (hh:MM:ss) for the start of the interval.
    end_time - a time (hh:MM:ss) for the end of the interval.

    :returns
    the number of posts between the given interval
    """
    start_time = pd.Timestamp(f"1900-01-01 {start_time}")
    end_time = pd.Timestamp(f"1900-01-01 {end_time}")
    start_time_mask = posts.post_time >= start_time
    end_time_mask = posts.post_time <= end_time
    interval_mask = start_time_mask & end_time_mask
    return len(posts.loc[interval_mask])
