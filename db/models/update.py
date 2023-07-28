class UPDATE_QUERY:
    @staticmethod
    def subscribers() -> str:
        return """
            UPDATE subreddit
            SET subscribers = %s
            WHERE name = %s;
        """
