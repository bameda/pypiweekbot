import sys

try:
    from . import local
except ImportError:
    sys.exit("Error: create settings file")

ACCESS_TOKEN = getattr(local, 'ACCESS_TOKEN', 'undefined')
ACCESS_SECRET = getattr(local, 'ACCESS_SECRET', 'undefined')
CONSUMER_KEY = getattr(local, 'CONSUMER_KEY', 'undefined')
CONSUMER_SECRET = getattr(local, 'CONSUMER_SECRET', 'undefined')

USER_BACK_LIST = getattr(local, 'USER_BACK_LIST', [])
WORD_BLACK_LIST = getattr(local, 'WORD_BLACK_LIST', [])

SEARCH_QUERY = getattr(local, 'SEARCH_QUERY', '#piweek')
