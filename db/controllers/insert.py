from db import pool, db
from db.models import INSERT_QUERY
from classes import Comment, Submission


class INSERT:
    @staticmethod
    def comment(comment: Comment) -> None:
        """
        Inserts a comment from Reddit.
        """

        try:
            pool.execute(
                INSERT_QUERY.comment(),
                (
                    comment.id,
                    comment.body,
                    comment.url,
                    comment.author,
                    comment.submission,
                    comment.subreddit,
                    comment.created_date
                )
            )

            db.commit()
        except Exception as e:
            print(f"Comment insertion error: {e}")

    @staticmethod
    def sumbission(submission: Submission) -> None:
        """
        Inserts a submission from Reddit.
        """
        try:
            pool.execute(
                INSERT_QUERY.submission(),
                (
                    submission.id,
                    submission.subreddit,
                    submission.title,
                    submission.body,
                    submission.score,
                    submission.author,
                    submission.url,
                    submission.created_date
                )
            )

            db.commit()
        except Exception as e:
            print(f"Submission insertion error: {e}")
    

    @staticmethod
    def comment_ticker(ticker: str, comment_id: str) -> None:
        """
        Inserts a submission from Reddit.
        """
        try:
            pool.execute(
                INSERT_QUERY.comment_ticker(),
                (
                    ticker,
                    comment_id
                )
            )

            db.commit()
        except Exception as e:
            print(f"Submission comment_ticker error: {e}")
