import sys
from app import RedditAPI
from db import GET
from util import timer
from settings import USER_AGENT


def main():
    headers = {
        "User-Agent": USER_AGENT
    }
    subreddit = "wallstreetbets"

    api = RedditAPI()

    response = api.hot(subreddit, headers=headers)
    data = response.json()["data"]
    submissions = data["children"]

    for sub in submissions:
        print(sub)
        print()



if __name__ == "__main__":
    timer(main)
