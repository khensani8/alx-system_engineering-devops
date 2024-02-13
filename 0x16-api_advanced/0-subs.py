#!/usr/bin/python3
"""Task 0 - a function queries the Reddit API and returns number of subs
    for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
     """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
     url = f"https://www.reddit.com/r/{subreddit}/about.json"
     headers = {"User-Agent": "YesYourBot"}
     response = requests.get(url, headers=headers)

     if response.status_code = 200:
        data = response.json()
        return data['data']['subscribers']
     
     else:
        return 0
        )