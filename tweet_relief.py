import tweepy
import json
from time import sleep
from gooey import Gooey, GooeyParser
from datetime import datetime
import os
import pytz


@Gooey(program_name='Tweet Relief', show_sidebar=False, disable_stop_button=True)

def main():
    desc = 'A simplified GUI for wiping your Twitter history'
    parser = GooeyParser(description=desc)
    
    creds_parser = parser.add_argument_group('First, enter your Twitter API credentials:', gooey_options={'show_border': False, 'columns': 2})
    creds_parser.add_argument('consumer_key', metavar='Consumer Key', widget='PasswordField')
    creds_parser.add_argument('consumer_secret', metavar='Consumer Secret:', widget='PasswordField')
    creds_parser.add_argument('access_token', metavar='Access Token:', widget='PasswordField')
    creds_parser.add_argument('access_token_secret', metavar='Access Token Secret:', widget='PasswordField')
    
    date_parser = parser.add_argument_group('Select your cutoff date')
    date_parser.add_argument('stop_date', metavar='Tweets published before this date will be deleted:', widget='DateChooser')

    keepers = parser.add_argument_group('Keeping any tweets?')
    keepers.add_argument('keepers', default='None', metavar='Enter tweet IDs you want to keep, separated by commas. (If not, leave as \'None\'.)')

    args = parser.parse_args()
    
    if args.keepers == 'None':
        if os.path.exists(os.path.join('data', 'keepers.json')):
            with open(os.path.join('data', 'keepers.json'), 'r') as j:
                keepers = json.load(j)
        else:
            pass
    else:
        keepers = trapper_keeper()
    
    api = authorize()
    tweets = get_all_tweets() 
    if keepers:
        nonkeepers = [tweet for tweet in tweets if tweet.id not in keepers]
        destroyer(nonkeepers) 
    else:
        destroyer(tweets)
  
  
def authorize():
    auth = tweepy.OAuthHandler(args.consumer_key, args.consumer_secret)
    auth.set_access_token(args.access_token, args.access_token_secret)
    return tweepy.API(auth)

def trapper_keeper():
    splits = ','.split(args.keepers)
    splits = [int(tweet.strip()) for tweet in splits]
    if os.path.exists(os.path.join('data', 'keepers.json')):
        with open(os.path.join('data', 'keepers.json'), 'r') as j:
            exist_keepers = json.load(j)
        updated_keepers = exist_keepers.append(splits)
        with open(os.path.join('data', 'keepers.json'), 'w') as j:
            json.dump(updated_keepers, j)
        return updated_keepers
    else:
        if os.path.exists('data'):
            with open(os.path.join('data', 'keepers.json'), 'w') as j:
                json.dump(splits, j)
            return splits
        else:
            os.mkdir('data')
            with open(os.path.join('data', 'keepers.json'), 'w') as j:
                json.dump(splits, j)
            return splits


def get_all_tweets():
    screen_name = (api.me()).screen_name
    all_tweets = []
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)
    all_tweets.extend(new_tweets)
    oldest = alltweets[-1].id - 1
    while len(new_tweets) > 0:
        new_tweets = api.user_timeline(screen_name=xx, count=200, max_id=oldest)
        all_tweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1
        print('{0} tweets grabbed so far...'.format(len(all_tweets)))
        sleep(2)
    print('Grabbed {0} tweets...'.format(len(all_tweets))
    return all_tweets


def destroyer(tweet_objects):
    print('Destroying tweets... This might take a while.')
    cutoff_date = utc.localize(datetime.strptime(args.stop_date, '%Y-%m-%d'))
    destroyed = []
    for tweet in tweet_objects:
        create_date = datetime.strptime(tweet.created_at, "%a %b %d %H:%M:%S %z %Y")
        if create_date < cutoff_date:
            api.destroy_status(tweet.id)
            print('Tweet destroyed: {0}'.format(tweet.id))
            destroyed.append(tweet.id)
            sleep(0.1)
        else:
            pass
    print('Destruction complete, scrubbed {0} tweets from your timeline.'.format(len(destroyed)))


if __name__ == "__main__":
    main()
