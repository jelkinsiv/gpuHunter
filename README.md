# gpuHunter

Get push notifications if a new GPU is for sale on r/buildapcsales

## Why?

I'm trying to find a buy GPU but due to cryptomining they are hard to find in stock and for MSRP. 
This uses praw to get a list of the latest GPU for sale from r/buildapcsales. It then uses crump 
to send a push notifications

## Requirement

#### Pushover

- Go to [Pushover](https://pushover.net/) and create an account.
- Create a new App inside pushover to get the app secret.

#### Reddit
- Go to [reddit.com/prefs/apps](https://www.reddit.com/prefs/apps) and create a new app.

## Install

Navigate to the python files and install
```buildoutcfg
python setup.py install
```

You'll also need to make it executable
```buildoutcfg
chmod +x
```

Finally, you'll need to override the variables being imported from config.py or create a config.py 
and fill it out with the secrets from Pushover and reddit.
```buildoutcfg
PUSHOVER_APP_SECRET = ''
PUSHOVER_USER_SECRET = ''
REDDIT_CLIENT_ID = ''
REDDIT_CLIENT_SECRET = ''
REDDIT_USER_AGENT = ''
```

## How to use

I setup a cron job on a raspberry pi to run the script every 15 minutes and set the 'check_interval'
for the same 15 minutes. If you want to run faster or slower, make sure that update the 'check_intarval'
in '\_\_main__'
