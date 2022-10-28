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


def find_avg_post_time(posts: pd.DataFrame, profiles: pd.DataFrame):
    filtered_posts = posts.dropna()
    filtered_posts = filtered_posts[filtered_posts.profile_id.isin(profiles.profile_id)]
    sorted_posts = filtered_posts.sort_values(by='profile_id')
    profiles_with_posts = profiles[profiles.profile_id.isin(sorted_posts.profile_id.unique())]
    profiles_with_posts['true_n_posts'] = sorted_posts.groupby('profile_id')['profile_id'].count().values

    sorted_post_times = sorted_posts.cts.values

    # Find the indeces that will be used for finding posts
    profiles_with_posts['start_index'] = profiles_with_posts.true_n_posts.shift(1).cumsum().astype('Int64')
    profiles_with_posts.iloc[0, -1] = 0

    def find_max_min_time_stamps(profile_id, n_posts, start_index):
        """Finds the max and minimum post times in the sorted_post_times dataframe."""
        start_index = int(start_index)
        n_posts = int(n_posts)
        profile_post_times = sorted_post_times[start_index:start_index + n_posts]

        min_post_time = profile_post_times.min()
        max_post_time = profile_post_times.max()

        return max_post_time, min_post_time

    max_post, min_post = np.vectorize(find_max_min_time_stamps)(profiles_with_posts.profile_id, \
                                                                profiles_with_posts.true_n_posts, \
                                                                profiles_with_posts.start_index)

    profiles_with_posts['max_post'] = max_post
    profiles_with_posts['min_post'] = min_post

    profiles_with_posts['post_time_delta'] = profiles_with_posts.max_post - profiles_with_posts.min_post
    profiles_with_posts['avg_post_delta'] = profiles_with_posts.post_time_delta / (profiles_with_posts.true_n_posts - 1)

    return profiles_with_posts
