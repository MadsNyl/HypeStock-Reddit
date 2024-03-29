from dataclasses import dataclass
from datetime import datetime


@dataclass
class Comment:
    id: str
    body: str
    url: str
    author: str
    submission: str
    subreddit: str
    created_date: datetime
    collected_date: datetime = None
