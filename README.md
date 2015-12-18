# pyticli

A twitter bot (initially for @\_piweek\_ account).


## Setup

```
mkvirtualenv -p /usr/bin/python3 pyticli
workon pyticli
pip install -r requirements.txt
```

## Usage

```bash
$ ./pyticli --help

Usage: pyticli [OPTIONS]

  I'm a Twitter bot and I know how to do retweets.

  Make no mistake, I have my little heart too ;-)

Options:
  --access_token TEXT     Twitter access token (env. TWITTER_ACCESS_TOKEN)
  --access_secret TEXT    Twitter access secret (env. TWITTER_ACCESS_SECRET)
  --consumer_key TEXT     Twitter consumer key (env. TWITTER_CONSUMER_KEY)
  --consumer_secret TEXT  Twitter consumer secret (env. TWITTER_CONSUMER_SECRET)

  --user_blacklist TEXT   Users blacklist [multi] (env. TWITTER_USER_BLACKLIST)
  --word_blacklist TEXT   Words blacklist [multi] (env. TWITTER_WORD_BLACKLIST)
  --search_query TEXT     Search query (env. TWITTER_SEARCH_QUERY)

  --help                  Show this message and exit.
```

You can configure the bot with:

- command options.
- environment variables.
- using ```settings/local.py``` (example at ```settings/local.py.example```).
