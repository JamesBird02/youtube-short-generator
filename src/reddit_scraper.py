import praw
import os
import sys
import re
from dotenv import load_dotenv

load_dotenv()


def clean_and_format_title(title):
    cleaned_title = re.sub(r'[^\x00-\x7F]+', ' ', title)  # Remove non-ASCII characters
    cleaned_title = re.sub(r'\s+', ' ', cleaned_title).strip()

    return cleaned_title   
        

def fetch_posts(subreddit_name, limit=15):
    reddit = praw.Reddit(
        client_id = os.environ["my_client_id"],
        client_secret= os.environ["my_client_secret"],
        user_agent= os.environ["my_user_agent"],
        username= os.environ["my_username"],
        password= os.environ["my_password"],
    )

    subreddit = reddit.subreddit("geopolitics")
    posts = []
    for submission in subreddit.hot(limit=15):
        posts.append(submission)
    return posts


def get_user_input(subreddit_name="geopolitics"):
    f_posts = fetch_posts(subreddit_name)
    
    # Display the posts for user selection
    for index, submission in enumerate(f_posts, start=1):
        print(f"{index}: {clean_and_format_title(submission.title)}")
    
    try:
        selected_index = int(input("\nEnter the index of the post you want to create a video from: ")) - 1
        if selected_index < 0 or selected_index >= len(f_posts):
            print("Invalid selection. Exiting...")
            sys.exit()
    except ValueError:
        print("Please enter a valid number. Exiting...")
        sys.exit()

    selected_submission = f_posts[selected_index]
    title = selected_submission.title
    post_content = clean_and_format_title(selected_submission.selftext)
    return title, post_content
