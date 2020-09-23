import flask
import os
import requests
import tweepy
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys

API_KEY = os.environ['API_KEY']
API_KEY_SECRET = os.environ['API_KEY_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET'] 

auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

celebrity = 'Cristiano'
item = api.get_user(celebrity)

lst = []

end_date = datetime.utcnow() - timedelta(days=30)
for tweet in tweepy.Cursor(api.user_timeline, id=celebrity).items():
    if tweet.created_at < end_date:
        break
    lst.append(tweet.text)
    
lent = len(lst)   
app = flask.Flask(__name__)

@app.route('/')
def index():
     return flask.render_template(
        "index.html",
        list=lst,
        length=lent
        )
        
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)
    
    