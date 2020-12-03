import tweepy
import datetime
import csv

def gameDevEval(username, dateStart, dateEnd, fileName):
    gameTwitter = api.user_timeline(screen_name=username, count=200, include_rts=False, tweet_mode='extended')
    gameTweets = []  # Accumulates tweets
    for tweet in gameTwitter:
        if dateEnd > tweet.created_at > dateStart:
            gameTweets.append(tweet)

    while gameTwitter[-1].created_at > dateStart:
        gameTwitter = api.user_timeline(stardewUser, max_id=gameTwitter[-1].id, count=200, include_rts=False, tweet_mode='extended')
        for tweet in gameTwitter:
            if dateEnd > tweet.created_at > dateStart:
                gameTweets.append(tweet)

    csvFile = open(fileName + '.csv', 'w', newline='')  # Writes out results
    csvWriter = csv.writer(csvFile)
    for tweet in gameTweets:
        csvWriter.writerow([tweet.created_at, tweet.favorite_count, tweet.retweet_count, tweet.full_text.encode('utf-8')])
    csvFile.close()

# ****************
#  Main Function *
# ****************
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# ****************
# Stardew Valley *
# ****************
print("RESULTS FROM STARDEW VALLEY")
print("Dev Account - ConcernedApe")
stardewUser = "ConcernedApe"  # Hardcoded variables
stardewStart = datetime.datetime(2015, 12, 26, 0, 0, 0)  # 2 months before 2/26/2016
stardewEnd = datetime.datetime(2016, 4, 26, 0, 0, 0)  # 2 months after 2/26/2016
gameDevEval(stardewUser, stardewStart, stardewEnd, "stardewResult")

# ****************
#  Phasmophobia  *
# ****************
print("\nRESULTS FROM PHASMOPHOBIA")
print("Dev Account - KineticGame")
phobiaUser = "KineticGame"  # Hardcoded variables
phobiaStart = datetime.datetime(2020, 7, 18, 0, 0, 0)  # 2 months before 9/18/2020
phobiaEnd = datetime.datetime(2020, 11, 18, 0, 0, 0)  # 2 months after 9/18/2020
gameDevEval(phobiaUser, phobiaStart, phobiaEnd, "phobiaResult")

# ****************
#     Among Us   *
# ****************
print("\nRESULTS FROM AMONG US")
print("Dev Account - InnerslothDevs")
amongUser = "InnerslothDevs"  # Hardcoded variables
amongStart = datetime.datetime(2020, 6, 1, 0, 0, 0)  # 2 months before 8/1/2020
amongEnd = datetime.datetime(2020, 10, 1, 0, 0, 0)  # 2 months after 8/1/2020
gameDevEval(amongUser, amongStart, amongEnd, "amongUsResult")