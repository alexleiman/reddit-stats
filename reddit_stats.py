import praw
from datetime import datetime, timedelta
import pprint

reddit = praw.Reddit(client_id='zpMo4FrhS9AfuA',
                     client_secret='lew6Tc1DFZqQelj9F_Ith4J1jfE',
                     user_agent='pip3installpraw')


def get_comments(sub_name):
    """
    returns comments from the top 100 posts of
    the given subreddit
    """
    subreddit = reddit.subreddit(sub_name)
    posts = subreddit.top(time_filter='all')
    #http://praw.readthedocs.io/en/latest/code_overview/models/submission.html#praw.models.Submission.comments




td_comments = get_comments('The_Donald')
