# Tweet Relief
*With apologies to Doug Benson for stealing the name Tweet Relief.*

## What is it?
Tweet Relief is a Python script with a simple, Gooey-based GUI front to help scrub your Twitter profile of previous tweets. If you can run a Python script, you can wipe away your timeline.

<p align="center">
  <img src="https://dl.dropboxusercontent.com/s/tq1tgc0ddqbrp5q/window.png">
</p>

## Why tho?
Tweet Relief was inspired by a recent conversation in my Twitter DMs:

![cause.png](https://dl.dropboxusercontent.com/s/4bynphcbtqxwrl2/cause.png)

## What You'll Need:
- Python 3.5+
- Gooey and Tweepy libraries
- Twitter API credentials
- a burning desire to limit the spread of your Twitter persona

## Known Limitations
Currently, Twitter's API will only let you access the latest ~3,200 tweets on your timeline. If you have an extensive timeline, you'll need to re-run Tweet Relief in several passes. You don't don't have to worry about rate-limiting, though... The maximum number of timeline tweets you can pull in a single request is 200. The rate limit for *GET statuses/user_timeline* is 1500 requests per window, and since all Twitter GET request windows are 15 minutes in length, the ~3,200 access limit is *waaaaay* less than the max number of tweets you can pull down in a single window (300,000).

That being said, you *might* be rate-limited in deleting tweets. Twitter's [API documentation](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-destroy-id.html) states that deleting tweets is, like other API calls, rate-limited, but won't say exactly *what the limits are*. If you make a large number of passes on your timeline, beware that you might run afoul of some phantom API rate limit.

## How do I use it?
First, you'll need Python. If you already have Python, great –- skip to the next step. If you’re not sure, open whatever shell environment you use and type `python --version`. make sure it's Python 3.5 or newer.

Second, you’ll need to set up access to Twitter's API on your account. Go to [developer.twitter.com](https://developer.twitter.com), sign in with your Twitter account, and apply for building a new app. (Most likely, you will apply for a "hobbyist" account.)

Once you're approved, you'll obtain the four unique codes needed to interact with tweets programmatically:

- *Consumer Key*: required to authenticate your access (the 'client')
- *Consumer Secret*: the password for the client
- *Access Token*: defines what data the client can and cannot access
- *Access Token Secret*: the password for the Access Token

(Treat these four codes like the passwords that they are.) You’ll also need to set your app's Permissions tab to **Read and Write Access**.

Once you have your credentials, install the library dependencies for the script:
```
pip install -r requirements.txt
```
Then run the script as normal:
```
python tweet_relief.py
```

In the GUI, you'll add your credentials and pick a cutoff date; all tweets and retweets made before this cutoff date will be destroyed. You can also tell Tweet Relief which tweets that you don't deleted by adding their tweet IDs:

twitter.com/scottythered/status/ **1163158433865986048** ```<--- that's the tweet ID```

You only have to add these non-delete tweet IDs once -- Tweet Relief will generate a JSON file in the same directory and save your list of keepers, with the added bonus that it will update this list if you run Tweet Relief with new keepers in the future.

## Info, Questions and Comments
I am Scott Carlson, formerly the Metadata Coordinator of Rice University's Fondren Library. I received my MLIS from Dominican University (River Forest, IL) and an Archives Certificate in Digital Stewardship from Simmons College (Boston, MA). 
