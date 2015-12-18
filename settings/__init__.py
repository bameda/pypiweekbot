import sys

try:
    from . import local
except ImportError:
    local = {}
    print('No "settings/local.py" file found.', file=sys.stderr)


ACCESS_TOKEN = getattr(local, 'ACCESS_TOKEN', 'undefined')
ACCESS_SECRET = getattr(local, 'ACCESS_SECRET', 'undefined')
CONSUMER_KEY = getattr(local, 'CONSUMER_KEY', 'undefined')
CONSUMER_SECRET = getattr(local, 'CONSUMER_SECRET', 'undefined')

USER_BLACKLIST = getattr(local, 'USER_BLACKLIST', [])
WORD_BLACKLIST = getattr(local, 'WORD_BLACKLIST', [])

SEARCH_QUERY = getattr(local, 'SEARCH_QUERY', '#piweek')
