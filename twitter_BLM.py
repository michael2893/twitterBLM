import pandas as pd
import tweepy

## pip install tweepy
## pip install pandas for the dataframe

try:
    consumer_key = "esYHqOwZzrFxhNs4VWusCneM1"      ## my bots secret keys, i really don't care, USE it but be reasonable
    consumer_secret = "CkMWgyDYZwk1xBOnEIFXuKtZo98JCyvm2JnGFHqVH7vOblUHt6"
    access_token = "1258923150303285248-nxxBtoaDiV9ByhwxAPAhsW2Y1TUUo9"
    access_token_secret = "QHLvYoSPVzVHZXL6Hzd5Wibh4ALTRn0M05HekKAIKHaG4"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True)
    df = pd.DataFrame(columns=['text', 'user','account'])

    for status in tweepy.Cursor(api.user_timeline).items(): ## destroy tweets to make sure duplicates aren't an issue
            api.destroy_status(status.id)

    for tweet in tweepy.Cursor(api.search, q='#BlueLivesMatter AND #Trump AND #MAGA AND #AllLivesMatter -filter:retweets', rpp=100).items(10000):
        twt = [tweet.text, tweet.user.name, tweet.user.screen_name] 
        twt = tuple(twt)                    
        twt.append(twt)
        source = tweet.source_url
    df = pd.DataFrame(twt) ## new DF with the tweets pssed in
    df.drop_duplicates
    users = '@' + df[2] ## users are DF at index 2 prefixed with '@'

    for user_name in users:
        api.update_status(user_name + " " + "https://www.paypal.me/theokraproject")
        
## for all users send tweets

    df.to_csv('list.csv')
    ## convert to CSV

except tweepy.TweepError as error:
    if error.api_code == 187:
        print('duplicate message, it is fine') ## catch errors
    else:
        raise error
