#!/usr/bin/env python3

from datetime import datetime, timedelta
from chump import Application
import praw
from config import PUSHOVER_APP_SECRET, PUSHOVER_USER_SECRET, REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT


def hunt(check_interval):
    pushover_app = Application(PUSHOVER_APP_SECRET)
    pushover_user = pushover_app.get_user(PUSHOVER_USER_SECRET)

    reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                         client_secret=REDDIT_CLIENT_SECRET,
                         user_agent=REDDIT_USER_AGENT
                         )

    subreddit = reddit.subreddit('buildapcsales')
    min_delta = datetime.utcnow() - timedelta(minutes=check_interval)

    filtered_subs = [
        x for x in subreddit.new(limit=25)
        if datetime.utcfromtimestamp(x.created_utc) >= min_delta and "GPU" in x.title
    ]

    if filtered_subs:
        response_msg = ""
        for sub in filtered_subs:
            response_msg += "\n<a href=\"" + sub.shortlink + "\">" + sub.title + "</a>"

        if response_msg:
            push_notification = pushover_user.send_message(
                title="New GPU for sale",
                message=response_msg,
                html=True,
                sound='gamelan')


if __name__ == "__main__":
    hunt(16)
