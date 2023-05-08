import sys
from db import GET, INSERT
from app import get_legacy_comments, get_processed_data
from util import progressbar, timer


SUBREDDITS = GET.subreddits()
# SUBREDDITS = [
#     "wallstreetbets",
#     "stocks",
#     "stockmarket",
#     "investing",
#     "economy",
#     "economics",
#     "globalmarkets",
#     "options",
#     "finance",
#     "daytrading"
# ]


def main():
    days = 10
    limit = 100

    sub = sys.argv[1]

    if sub not in SUBREDDITS:
        return

    if len(sys.argv) > 2:
        days = int(sys.argv[2])

    if len(sys.argv) > 3:
        limit = int(sys.argv[3])

    TICKERS = GET.tickers()
    COMMENT_URLS = GET.comment_urls()

    progressbar(0, days, "Getting comments: ")
    for i, day in enumerate(reversed(range(days))):
        comments = get_legacy_comments(sub, day, day - 1, limit)

        for comment in comments:
            if comment["permalink"] in COMMENT_URLS:
                continue
            data = get_processed_data(comment, TICKERS)
            if data:
                INSERT.comment(data)
        progressbar(i + 1, days)


if __name__ == "__main__":
    timer(main)
