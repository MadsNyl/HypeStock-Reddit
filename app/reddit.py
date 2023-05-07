from settings import reddit
from db import GET, INSERT
from util import progressbar, remove_emojies
from classes import Comment
from datetime import datetime

class Reddit():
    
    _limit: int
    _subs: list[str]
    _comments: list[Comment] = []
    _tickers: dict[str: None]
    _comment_urls: dict[str: None]

    def __init__(self, subreddits: list[str], limit: int) -> None:
        self._subs = subreddits
        self._limit = limit
        self._tickers = GET.tickers()
        self._comment_urls = GET.comment_urls()
    
    def run(self) -> None:
        self._collect_posts()
        self._process_comments()

    def _collect_posts(self) -> None:
        progressbar(0, len(self._subs), "Collecting data: ")

        for i, sub in enumerate(self._subs):
            self._get_posts(sub)
            progressbar(i + 1, len(self._subs))
    
    def _get_posts(self, sub: object) -> None:
        subreddit = reddit.subreddit(sub)
        for post in self._get_subreddit_posts(subreddit, "hot"):
            post.comments.replace_more(limit=0)
            self._append_comments(post)
    
    def _get_subreddit_posts(self, subreddit: object, filter: str) -> list:
        match filter:
            case "hot": return subreddit.hot(limit=self._limit)
    
    def _append_comments(self, post: object) -> None:
        for comment in post.comments.list(): self._comments.append(comment)

    def _process_comments(self) -> None:
        progressbar(0, len(self._comments), "Processing comments: ")
        for i, comment in enumerate(self._comments):
            self._process_body(comment)
            progressbar(i + 1, len(self._comments))
    
    def _process_body(self, comment: object) -> None:
        body = remove_emojies(comment.body)
        for string in self._stripped_comment(body):
            if string in self._tickers:
                self._insert_comment(comment, string)
                break

    def _stripped_comment(self, comment: object) -> str: return comment.strip().split(" ")

    def _insert_comment(self, comment: object, ticker: str) -> None:
        if comment.permalink in self._comment_urls: return

        INSERT.comment(Comment(
            comment.permalink,
            ticker,
            comment.submission.permalink,
            comment.subreddit.display_name,
            datetime.fromtimestamp(comment.created),
            comment.score,
            remove_emojies(comment.body),
            comment.author.name if comment.author else None      
        ))