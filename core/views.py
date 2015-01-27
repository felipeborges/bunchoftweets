from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

import twitter
import json

api = twitter.Api(consumer_key = 'XXXXXXXXXXXXXXXXXXXXXXXXX',
                  consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXX',
                  access_token_key = 'XXXXXXXXXXXXXXXXXXXXXXXXX',
                  access_token_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXX')



def index(request):
    return render(request, 'bunchoftweets/index.html', {}, content_type = 'text/html')

def get_tweets(request, tweets_id):
    tweets = []
    tweet_objs = tweets_id.split(',')

    for tweet_id in tweet_objs:
        json_status = api.GetStatus(int(tweet_id), include_entities = False)
        tweet = json.loads(str(json_status))
        tweets.append(tweet)

    return render(request,
                  'bunchoftweets/tweets.html',
                  {
                      'tweets': tweets,
                  },
                  content_type = "text/html")
