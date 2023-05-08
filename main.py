import sys
from app import Reddit
from db import GET
from util import timer


def main():
    subs = GET.subreddits()
    limit = 5

    if len(sys.argv) > 1:
        limit = int(sys.argv[1])

    r = Reddit(subs, limit)
    r.run()


if __name__ == "__main__":
    timer(main)
