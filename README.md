# Tweet-Relief
*With apologies to Doug Benson for stealing the name Tweet Relief.*

## What is it?
Tweet Relief is a Python script with a simple, Gooey-based GUI front to help scrub your Twitter profile of previous tweets.

## Why tho?
Who's to say why we do anything? Seriously though, Tweet Relief was inspired by a recent conversation in my Twitter DMs:

![cause.png](https://dl.dropboxusercontent.com/s/4bynphcbtqxwrl2/cause.png)

## What You'll Need:
- Python 3.5+
- Twitter API credentials
- a burning desire to limit the spread of your Twitter persona

## How do I use it?
First, you'll need Python. If you already have Python, great –- skip to the next step. If you’re not sure, open whatever shell environment you use and type `python --version`. make sure it's Python 3.5 or newer.

Second, you’ll need to set up access to Twitter's API on your account. Go to [developer.twitter.com](https://developer.twitter.com), sign in with your Twitter account, and apply for building a new app. (Most likely, you will apply for a "hobbyist" account.)

Once you're approved, you'll obtain the four unique codes needed to interact with tweets programmatically:

* *Consumer Key*: required to authenticate your access (the 'client')
* *Consumer Secret*: the password for the client
* *Access Token*: defines what data the client can and cannot access
* *Access Token Secret*: the password for the Access Token

Treat these four codes like the passwords that they are.

You’ll also need to set your app's Permissions tab to **Read and Write Access**.

Once you have your credentials, install the dependencies for the script:

```
pip install -r requirements.txt
```
