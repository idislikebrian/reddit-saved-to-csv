import praw, csv, codecs
import os
from notion.client import NotionClient

client = NotionClient(token_v2="") #Obtain the `token_v2` value by inspecting your browser cookies on a logged-in session on Notion.so
page = client.get_block("") #replace the URL with the URL of the page or databse you want to edit

client_id = '' # Enter your client ID
client_secret = '' # Enter you client secret
username = '' # Enter Username
password= '' # Enter password

reddit = praw.Reddit(client_id=client_id,
                    client_secret=client_secret,
                    user_agent='Saved posts scraper by /u/' + username,
                    username=username,
                    password=password)

reddit_home_url = 'https://www.reddit.com'

saved_models = reddit.user.me().saved(limit=None) # models: Comment, Submission

def handle(saved_models):
    count = 1
    for model in saved_models:
        subreddit = model.subreddit # Subreddit model that the Comment/Submission belongs to
        subr_name = subreddit.display_name
        url = reddit_home_url + model.permalink

        cv = client.get_collection_view("") #URL of table page
        row = cv.collection.add_row() # Add a new record to Notion

        if isinstance(model, praw.models.Submission): # if the model is a Submission
            title = model.title
            noSfw = str(model.over_18)
            model_type = "#Post"
        else: # if the model is a Comment
            title = model.submission.title
            noSfw = str(model.submission.over_18)
            model_type = "#Comment"
        
        row.id = count
        row.Name = title
        row.Subreddit = subr_name
        row.Type = model_type
        row.URL = url
        
        count += 1

handle(saved_models)

print("Your saved posts are available in Notion.")
