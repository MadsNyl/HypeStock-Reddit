class GET_QUERY:
    @staticmethod
    def tickers() -> str:
        return """
            SELECT symbol 
            FROM stock
        """

    @staticmethod
    def subreddits() -> str:
        return """
            SELECT DISTINCT subreddit
            FROM comment
        """

    @staticmethod
    def comment_urls() -> str:
        return """
            SELECT permalink
            FROM comment
        """
