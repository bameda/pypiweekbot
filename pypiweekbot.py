#!/usr/bin/env python3

import tweepy, hashlib, os

import settings


# build savepoint path + file
hashed_hashtag = hashlib.md5(bytes(settings.SEARCH_QUERY, "utf8")).hexdigest()
last_id_filename = 'last_id_hashtag_{}'.format(hashed_hashtag)
rt_bot_path = os.path.dirname(os.path.abspath(__file__))
last_id_file = os.path.join(rt_bot_path, last_id_filename)

# create bot
auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_SECRET)
api = tweepy.API(auth)


# retrieve last savepoint if available
try:
    with open(last_id_file, 'r') as file:
        savepoint = file.read()
except IOError:
    savepoint = ''
    print('ERROR: No savepoint found. Trying to get as many results as possible.')

# search query
timelineIterator = tweepy.Cursor(api.search,
				 q=settings.SEARCH_QUERY,
				 since_id=savepoint).items()

# put everything into a list to be able to sort/filter
timeline = []
for status in timelineIterator:
    timeline.append(status)

try:
    last_tweet_id = timeline[0].id
except IndexError:
    last_tweet_id = savepoint

# filter @replies/blacklisted words & users out and reverse timeline
timeline = filter(lambda status: status.text[0] != '@', timeline)
timeline = filter(lambda status: not any(word in status.text.split() for word in settings.WORD_BLACK_LIST), timeline)
timeline = filter(lambda status: status.author.screen_name not in settings.USER_BACK_LIST, timeline)
timeline = reversed(list(timeline))

# iterate the timeline and retweet
tw_counter = 0
err_counter = 0
for status in timeline:
    try:
        print('[{date}] - {name}: {message}'.format(date=status.created_at,
                                                      name=status.author.screen_name,
                                                      message=status.text))

        api.retweet(status.id)
        tw_counter += 1
    except tweepy.error.TweepError as e:
        # just in case tweet got deleted in the meantime or already retweeted
        err_counter += 1
        continue

print('Finished. {} Tweets retweeted, {} errors occured.'.format(tw_counter, err_counter))

# write last retweeted tweet id to file
with open(last_id_file, 'w') as file:
    file.write(str(last_tweet_id))
