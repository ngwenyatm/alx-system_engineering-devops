#!/usr/bin/python3
"""
query a list of all hot posts on a given Reddit subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddi
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {"count": count,"after": after,"limit": 100}
    response = requests.get(url, headers=headers, params=params,allow_redirects=False)
  
    if response.status_code == 404:
        return None
      
    results = response.json().get("data")
    count += results.get("dist")
    after = results.get("after")
  
    for kid in results.get("children"):
        hot_list.append(kid.get("data").get("title"))
      
    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
