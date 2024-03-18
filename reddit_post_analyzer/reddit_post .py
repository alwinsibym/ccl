import praw
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def categorize_sentiment(comment_text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_score = analyzer.polarity_scores(comment_text)['compound']

    if sentiment_score >= 0.05:
        return 'positive'
    elif sentiment_score <= -0.05:
        return 'negative'
    else:
        return 'neutral'

def reddit_post_analyzer(client_id, client_secret, user_agent, post_url):
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         user_agent=user_agent)

    submission = reddit.submission(url=post_url)
    submission.comments.replace_more(limit=None)

    comments_sentiments = {'positive': [], 'negative': [], 'neutral': []}

    for comment in submission.comments.list():
        sentiment = categorize_sentiment(comment.body)
        comments_sentiments[sentiment].append(comment.body)

    return comments_sentiments

if __name__ == "__main__":
    
    CLIENT_ID =  '0ciF6VCPCXEETK-u4Kv6nQ'
    CLIENT_SECRET = '-iHztq092K8l6kMldtGRGEPcFsPb-Q'
    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Brave/97.0.4692.71'


   
    POST_URL = 'https://www.reddit.com/r/marvelstudios/comments/1bhgfjh/rewatching_infinity_war_and_loved_all_over_again/'

   
    sentiments = reddit_post_analyzer(CLIENT_ID, CLIENT_SECRET, USER_AGENT, POST_URL)

    
   # Print the results
print("\nPositive Comments:")
for comment in sentiments['positive']:
    print(comment)
    print("\n")

print("\nNegative Comments:")
for comment in sentiments['negative']:
    print(comment)
    print("\n")

print("\nNeutral Comments:")
for comment in sentiments['neutral']:
    print(comment)
    print("\n")

