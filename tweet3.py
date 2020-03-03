import tweepy
import csv
import json


consumer_key = "a8rYAmN5yQdhwPQiAXfTy3w50"
consumer_secret = "b6KKMSVP4PhWFCcCBz8OCYHg0JF6JL0Kra1opS0tLXc9sHDG3m"
access_token = "2889380456-L1UStc3byGMd8M3G1cl3XVQJZw9S9nbzDnDoopO"
access_token_secret = "HIzBe0eYjYLCmzNcqjWG4ln3cw0Se46cVJAdgLudrq7i5"


    #create authentication for accessing Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

    #initialize Tweepy API
api = tweepy.API(auth)







maximum_number_of_tweets_to_be_extracted = int(input('Enter the number of tweets that you want to extract- '))

# Mention the hashtag that you want to look out for

hashtag = input('Enter the hashtag you want to scrape- ')



#we reate a list form of only id, date of creation, and text from the tweets that will be downloaded. 
#this is important because there are part of the tweets like the status, that cant be looped through. With this
#we make sure that we loop through it. 


outtweets = [[tweet.id_str, tweet.created_at,
                 tweet.text.encode('utf-8')] for tweet in tweepy.Cursor(api.search, q='#' + hashtag,
                           rpp=100).items(maximum_number_of_tweets_to_be_extracted)]

# we create the csv document we are going to place the tweets into. 
with open( hashtag + '_tweets.csv', 'w', encoding='utf8') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'created_at', 'text'])
    writer.writerows(outtweets)

print('downloaded' + str(maximum_number_of_tweets_to_be_extracted) + 'tweets')

