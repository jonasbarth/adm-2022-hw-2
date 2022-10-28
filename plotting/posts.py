"""A module containing functions for plotting data related to instagram datasets for ADM HW 2."""
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
from matplotlib.colors import LogNorm

from posts import find_number_of_posts_between


def plot_post_frequency(times, frequencies, max_time):
    """Function that plots the post frequency over time.
    
    :arg
    times - an iterable containing post times
    frequencies - an iterable containing the frequencies for each time
    max_time - the time where the posting frequency is highest

    """
    xformatter = mdates.DateFormatter('%H:%M')
    fig, ax = plt.subplots(nrows=1, ncols=1)
    fig.set_size_inches(10, 4)

    ax.plot_date(times, frequencies)
    ax.xaxis.set_major_formatter(xformatter)
    ax.axvline(x = max_time, color = 'orange')
    ax.text(x = max_time, y = min(frequencies), s = str(max_time)[11:], color = 'orange')
    ax.set_xlabel('Time of Day', fontsize=10);
    ax.set_ylabel('Number of Posts', fontsize=10);
    ax.set_title('The frequency of posts per hour');


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

    interval_labels = interval_labels[::-1]
    number_of_posts = number_of_posts[::-1]
    plt.barh(interval_labels, number_of_posts)
    plt.title("Number of posts per time interval")
    plt.xlabel("Number of posts")
    plt.ylabel("Time interval")
    plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',')))


def plot_followers_following_post_freq(followers, following, frequency, log, title):
    """Plots the number of followers, following, and posting frequency."""

    if log:
        plt.figure(figsize=(15, 10), dpi=80)
        plt.scatter(frequency, followers, c=following, norm=LogNorm(), s=1)
        plt.yscale('log')
        plt.xscale('log')
    else:
        plt.scatter(frequency, followers, c=following)

    plt.title(title)
    plt.xlabel('Average number of seconds between posts')
    plt.ylabel('Number of followers')

    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

    plt.colorbar(label='Number of following');


def plot_likes_comments_for_intervals(intervals, likes, comments):
    """Plots a vertical bar chart with grouped bars of likes and comments for each interval."""
    label_locations = np.arange(len(intervals))
    bar_width = 0.35

    fig, ax = plt.subplots()
    fig.set_size_inches(10, 8)

    bar_likes = ax.barh(label_locations - bar_width / 2, likes, bar_width, label='Average number of likes')
    bar_comments = ax.barh(label_locations + bar_width / 2, comments, bar_width, label='Average number of comments')

    ax.set_ylabel('Time intervals')
    ax.set_yticks(label_locations, intervals)

    ax.set_xlabel('Count')
    ax.set_title('Average number of likes and comments per time interval')
    ax.legend()

    ax.bar_label(bar_likes, padding=3)
    ax.bar_label(bar_comments, padding=3)

    fig.tight_layout()

    plt.show()