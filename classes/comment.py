class Comment:
    permalink: str
    symbol: str
    post_url: str
    subreddit: str
    created_date: str
    likes: int
    body: str
    author: str

    def __init__(
        self,
        permalink: str,
        symbol: str,
        post_url: str,
        subreddit: str,
        created_date: str,
        likes: int,
        body: str,
        author: str,
    ) -> None:
        self.permalink = permalink
        self.symbol = symbol
        self.post_url = post_url
        self.subreddit = subreddit
        self.created_date = created_date
        self.likes = likes
        self.body = body
        self.author = author
