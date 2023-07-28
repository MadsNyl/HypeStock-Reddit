from db import pool
from db.models import GET_QUERY


class GET:
    @staticmethod
    def tickers() -> dict:
        """
        Returns all tickers as a dict.
        """

        try:
            pool.execute(GET_QUERY.tickers())

            return dict.fromkeys(list(map(lambda x: x[0], pool.fetchall())))

        except Exception as e:
            print(f"Fetching all tickers error: {e}")
        
    @staticmethod
    def homographs() -> dict:
        """
        Returns all tickers as a dict.
        """

        try:
            pool.execute(GET_QUERY.homographs())

            return dict.fromkeys(list(map(lambda x: x[0], pool.fetchall())))

        except Exception as e:
            print(f"Fetching all homographs error: {e}")

    @staticmethod
    def subreddits() -> list:
        """
        Returns all subreddits as a list:
        """

        try:
            pool.execute(GET_QUERY.subreddits())

            return list(map(lambda x: x[0], pool.fetchall()))
        except Exception as e:
            print(f"Fetching all subreddits: {e}")

    @staticmethod
    def comment_urls() -> dict:
        """
        Returns all comment urls as a dict.
        """

        try:
            pool.execute(GET_QUERY.comment_urls())

            return dict.fromkeys(list(map(lambda x: x[0], pool.fetchall())))
        except Exception as e:
            print(f"Fetching comment urls error: {e}")
    
    @staticmethod
    def config_url():
        """
        Returns the url of the config.
        """
        try:
            pool.execute(GET_QUERY.config_url(), ("config.json", ))

            return pool.fetchone()[0]
        except Exception as e:
            print(f"Fetching config url error: {e}")
