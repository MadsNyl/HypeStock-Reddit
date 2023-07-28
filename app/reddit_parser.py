from datetime import datetime


class RedditParser():
    

    def get_data(self, data: dict) -> dict:
        return data["data"]

    def subscribers(self, data: dict) -> int:
        return data["subscribers"]
    
    def children(self, data: dict) -> list[dict]:
        return data["children"]
    
    def url(self, data: dict) -> str:
        try:
            permalink = data["data"]["permalink"]
            return f"https://reddit.com{permalink}"
        except Exception as e:
            print("Error collecting subbmission url.")
    
    def submission_body(self, data: dict) -> str:
        return data["data"]["selftext"]
        
    def body(self, data: dict) -> str:
        return data["data"]["body"]
    
    def title(self, data: dict) -> str:
        return data["data"]["title"]
    
    def score(self, data: dict) -> int:
        return data["data"]["score"]
        
    def created_date(self, data: dict) -> datetime:
        timestamp = data["data"]["created"]
        return datetime.fromtimestamp(timestamp)
            
    def id(self, data: dict) -> datetime:
        return data["data"]["id"]
                
    def author(self, data: dict) -> datetime:
        return data["data"]["author"]