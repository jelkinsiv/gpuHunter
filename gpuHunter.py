#!/usr/bin/env python

from datetime import datetime, timedelta
from functools import reduce
from chump import Application
import praw
from config import PUSHOVER_APP_SECRET, PUSHOVER_USER_SECRET, REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT

checkMin = 150

pushoverApp = Application(PUSHOVER_APP_SECRET)
pushoverUser = pushoverApp.get_user(PUSHOVER_USER_SECRET)

reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                     client_secret=REDDIT_CLIENT_SECRET,
                     user_agent=REDDIT_USER_AGENT
                     )


def main():

    subreddit = reddit.subreddit('buildapcsales')
    min_delta = datetime.utcnow() - timedelta(minutes=checkMin)

    filtered_subs = [
        x for x in subreddit.new(limit=25)
        if datetime.utcfromtimestamp(x.created_utc) >= min_delta and "[GPU]" in x.title
    ]

    title_list = list(map(lambda x: x.title, filtered_subs))
    if title_list:
        response_msg = reduce(lambda x, y: x + "\n" + y, title_list)
        print(response_msg)

        if response_msg:
            push_notification = pushoverUser.send_message(
                title="New GPU for sale",
                message="<b>" + response_msg + "</b>",
                html=True,
                sound='gamelan')

if __name__ == "__main__":
    main()