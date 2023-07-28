from db import pool, db
from db.models import UPDATE_QUERY


class UPDATE:
    @staticmethod
    def subscribers(subscribers: int, subreddit: str) -> dict:
        """
        Updates subscribers for given subreddit.
        """

        try:
            pool.execute(
                UPDATE_QUERY.subscribers(),
                (subscribers, subreddit)
            )

            db.commit()
        except Exception as e:
            print(f"Updating subscibers of subreddit error: {e}")