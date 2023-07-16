from requests import Response
from util import http_get


class RedditAPI():
    host: str = "https://reddit.com"

    def hot(self, subreddit: str, limit: int = 12, **kwargs) -> Response:
        query = f"{self.host}/r/{subreddit}/hot.json?limit={limit}"
        return http_get(query, **kwargs)
    
    def best(self, subreddit: str, limit: int = 12, **kwargs) -> Response:
        query = f"{self.host}/r/{subreddit}/best.json?limit={limit}"
        return http_get(query, **kwargs)
    
    def top(self, subreddit: str, limit: int = 12, **kwargs) -> Response:
        query = f"{self.host}/r/{subreddit}/top.json?limit={limit}"
        return http_get(query, **kwargs)
    
    def new(self, subreddit: str, limit: int = 12, **kwargs) -> Response:
        query = f"{self.host}/r/{subreddit}/new.json?limit={limit}"
        return http_get(query, **kwargs)

    def rising(self, subreddit: str, limit: int = 12, **kwargs) -> Response:
        query = f"{self.host}/r/{subreddit}/rising.json?limit={limit}"
        return http_get(query, **kwargs)
    
    def controversial(self, subreddit: str, limit: int = 12, **kwargs) -> Response:
        query = f"{self.host}/r/{subreddit}/controversial.json?limit={limit}"
        return http_get(query, **kwargs)

    def submission(self, id: str, **kwargs) -> Response:
        query = f"{self.host}/by_id/{id}.json"
        return http_get(query, **kwargs)

    def submission_comments(self, id: str, limit: int = 12, **kwargs) -> Response:
        query = f"{self.host}/comments/{id}.json?limit={limit}"
        return http_get(query, **kwargs)

    def subreddit_comments(self, subreddit: str, limit: int = 12, **kwargs) -> Response:
        query = f"this.host/r/{subreddit}/comments.json?limit={limit}"
        return http_get(query, **kwargs)