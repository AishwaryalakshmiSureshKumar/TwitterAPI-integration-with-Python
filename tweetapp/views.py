#import modules
import json
from django.http.response import JsonResponse
from django.conf import settings
import tweepy

#function to set twitter authentication
def twitter_auth():

    auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
    auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)

    return auth


#function to define twitter client api
def get_twitter_client():

    auth = twitter_auth()
    client = tweepy.API(auth, wait_on_rate_limit=True)

    return client


#function to scrape tweets by Hashtag
def getTweetsByHashtag(request, searchword):
    
    try:
        limit = request.GET.get('limit')
        searchword = '#'+searchword

        #setting default limit
        if limit is None:
            limit = 30
        
        client = get_twitter_client()
        
        #using tweepy module to extract tweets by hashtag
        tweets = tweepy.Cursor(client.search_full_archive,label='FullArchive',
                query=searchword).items(limit)
        
        list_tweets = [tweet._json for tweet in tweets]

        #converting as json string
        json_strings = [json.dumps(json_obj) for json_obj in list_tweets] 
        
        print(json_strings)

    except Exception:
        print({"error":True, "msg":"No Tweets Found"}, status=400)


#function to get user specific tweets
def getTweetsByUser(request, user):

    try:
        limit = request.GET.get('limit')

        #setting default limit
        if limit is None:
            limit = 30

        client = get_twitter_client()

        user_tweets = []

        #using tweepy module to extract tweets based on user
        for status in tweepy.Cursor(client.home_timeline, screen_name=user).items(limit):
            user_tweets.append(status._json)

        #converting as json string
        json_strings = [json.dumps(json_obj) for json_obj in user_tweets]

        print(json_strings)

    except Exception:
        print({"error":True, "msg":"No Tweets Found for the User"}, status=400)


