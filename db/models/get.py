class GET_QUERY:
    @staticmethod
    def tickers() -> str:
        return """
            SELECT symbol 
            FROM ticker
        """
    
    @staticmethod
    def homographs() -> str:
        return """
            SELECT word 
            FROM article_word
        """

    @staticmethod
    def subreddits() -> str:
        return """
            SELECT DISTINCT name
            FROM subreddit
        """

    @staticmethod
    def comment_urls() -> str:
        return """
            SELECT url
            FROM reddit_comment
        """

    @staticmethod
    def config_url() -> str:
        return """
            SELECT url
            FROM config_file
            WHERE name = %s;
        """
