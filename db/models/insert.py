class INSERT_QUERY:

    @staticmethod
    def comment() -> str:
        return """
            INSERT INTO reddit_comment
            (id, body, url, author, submission, subreddit, created_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
    
    @staticmethod
    def submission() -> str:
        return """
            INSERT INTO submission
            (id, subreddit, title, body, score, author, url, created_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """
    
    @staticmethod
    def comment_ticker() -> str:
        return """
            INSERT INTO reddit_ticker
            (ticker, comment)
            VALUES (%s, %s);
        """
