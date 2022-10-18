"""Module that contains functions for the times at which users publish their posts"""
import pandas as pd
import matplotlib.pyplot as plt

def most_common_time(posts : pd.DataFrame):
    """Returns the most common time at which users publish their posts.

    :arg
    posts - a pandas dataframe containing the times at which users post.

    :returns
    the most common publishing post time found in the posts dataframe
    """
    most_common_datetime = posts.post_time.value_counts().idxmax()
    return f"{most_common_datetime.hour}:{most_common_datetime.minute}:{most_common_datetime.second}"


def date_time_to_time(datetime):
    """Removes the date from the datetime object and returns a time in format HH:MM:SS."""

    hour = f"{datetime.hour}" if datetime.hour > 9 else f"{0}{datetime.hour}"
    minutes = f"{datetime.minute}" if datetime.minute > 9 else f"{0}{datetime.minute}"
    seconds = f"{datetime.second}" if datetime.second > 9 else f"{0}{datetime.second}"

    return f"{hour}:{minutes}:{seconds}"


def plot_posts_intervals(posts : pd.DataFrame, intervals):
    """Returns a plot with the number of posts for each given interval.

    :arg
    posts - a pandas dataframe containing the times at which users post.
    intervals - a list of tuples where each tuple contains the start and end time (start, end).

    :return
    a plot
    """

    intervals_labels, number_of_posts = find_posts_between(posts, intervals)

    return plt.barh(intervals_labels, number_of_posts)



def find_posts_between(posts : pd.DataFrame, intervals):
    """Finds posts with post times within the given list of inclusive intervals.

    :arg
    posts - a pandas dataframe containing the times at which users post.
    intervals - a list of tuples where each tuple contains the start and end time (start, end).

    :return
    intervals - a list of intervals as strings.
    number_of_posts - a list of number of posts, where the indeces match those of the intervals.
    """
    number_of_posts = [_find_posts_between(posts, start, end) for start, end in intervals]
    intervals_labels = list(map(lambda start, end : f"{start} - {end}"))
    return intervals_labels, number_of_posts


def _find_posts_between(posts : pd.DataFrame, start_time, end_time):
    """Finds posts between the given inclusive start and  inclusive end interval.

    :arg
    posts - a pandas dataframe containing the times at which users post.
    start_time - a time (hh:MM:ss) for the start of the interval.
    end_time - a time (hh:MM:ss) for the end of the interval.

    :returns
    the number of posts between the given interval
    """
    interval_mask = posts.post_time >= start_time and posts.posttime <= end_time
    return len(posts.loc[interval_mask])



