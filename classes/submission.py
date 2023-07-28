from dataclasses import dataclass
from datetime import datetime


@dataclass
class Submission():
    id: str
    subreddit: str
    title: str
    body: str
    score: int
    author: str
    url: str
    created_date: datetime
    collected_date: datetime = None
