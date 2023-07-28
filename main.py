from app import RedditAPI, RedditAPIAsync, RedditParser
from db import GET, UPDATE, INSERT
from util import timer, load_config_settings
from classes import Submission, Comment
from settings import USER_AGENT


VALID_TICKERS = GET.tickers()
TICKER_HOMOGRAPHS = GET.homographs()
COMMENT_URLS = GET.comment_urls()


def scrape(cap: int, subreddit: str):

    parser = RedditParser() 
    api = RedditAPI()
    headers = {
        "User-Agent": USER_AGENT
    }

    subreddit_response = api.subreddit(subreddit, headers=headers)
    subreddit_data = parser.get_data(subreddit_response.json())
    subscribers = parser.subscribers(subreddit_data)
    UPDATE.subscribers(subscribers, subreddit)

    submissions_response = api.hot(subreddit, headers=headers)
    data = parser.get_data(submissions_response.json())
    submissions = parser.children(data)

    for sub in submissions:
        sub_inserted = False

        submission_id = parser.id(sub)
        submission_body = parser.submission_body(sub)
        sumbission_tickers = get_tickers(submission_body)
        submission = Submission(
            subreddit = subreddit,
            url = parser.url(sub),
            body = submission_body,
            title = parser.title(sub),
            score = parser.score(sub),
            id = submission_id,
            author = parser.author(sub),
            created_date = parser.created_date(sub)   
        )

        if sumbission_tickers:
            INSERT.sumbission(submission)
            sub_inserted = True
            continue

        comments_response = api.submission_comments(submission_id, headers=headers).json()
        comments_response.pop(0)
        comments_data = parser.get_data(comments_response[0])
        comments = parser.children(comments_data)
        comments = comments[:-1]

        for comment in comments:
            url = parser.url(comment)

            if url in COMMENT_URLS:
                continue

            comment_id = parser.id(comment)

            body = parser.body(comment)
            comment_tickers = get_tickers(body)

            if comment_tickers:
                if not sub_inserted:
                    INSERT.sumbission(submission)
                    sub_inserted = True

                INSERT.comment(
                    Comment(
                        id=comment_id,
                        body=parser.body(comment),
                        url=parser.url(comment),
                        author=parser.author(comment),
                        submission=submission_id,
                        subreddit=subreddit,
                        created_date=parser.created_date(comment)
                    )
                )

                [
                    INSERT.comment_ticker(ticker, comment_id)
                    for ticker
                    in comment_tickers
                ]


def get_tickers(body: str) -> set[str]:
    body_text = body.split(" ")
    TICKERS = set()

    for word in body_text:
        if (
            word in VALID_TICKERS and
            word not in TICKER_HOMOGRAPHS
        ):
            TICKERS.add(word)

    return TICKERS


def main():
    config = load_config_settings()
    SUBREDDITS = GET.subreddits()

    cap = 15
    async_scraping = False

    if config:
        cap = config["reddit"]["limit"]
        async_scraping = config["reddit"]["async"]

    if async_scraping:
        api = RedditAPIAsync()
    else: 
        [scrape(cap, subreddit) for subreddit in SUBREDDITS]




if __name__ == "__main__":
    timer(main)
