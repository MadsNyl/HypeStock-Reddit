from db import pool, db
from db.models import INSERT_QUERY
from classes import Comment


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
                    comment.permalink,
                    comment.symbol,
                    comment.post_url,
                    comment.subreddit,
                    comment.created_date,
                    comment.likes,
                    comment.body,
                    comment.author,
                ),
            )

            db.commit()
        except Exception as e:
            print(f"Comment insertion error: {e}")
