class INSERT_QUERY:
    @staticmethod
    def comment() -> str:
        return """
            INSERT INTO comment
            (permalink, symbol, post_url, subreddit, created_date, likes, body, author)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
