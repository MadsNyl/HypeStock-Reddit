import requests
from util import remove_emojies, JSONObject, http_get_async
from classes import Comment


class PushShift():
    _BASE_URL: str = "https://api.pushshift.io./reddit"

    async def get_submissions(
        self,
        subreddit: str,
        start: str,
        end: str,
        limit: int
    ) -> list[JSONObject]:
        submission_url = "/search/submission/"
        subreddit_url = f"?subreddit={subreddit}"
        start_url = f"&after={start}d"
        end_url = f"&before={end}d"
        size_url = f"&size={limit}"
        url = f"{self._BASE_URL}{submission_url}{subreddit_url}{start_url}{end_url}{size_url}"

        print(url)
        headers = {"Accept": "application/json"}

        response = await http_get_async(url, headers=headers)
        print(response.text)
        

def get_legacy_comments(subreddit: str, start: str, end: str, limit: int) -> list[dict]:
    url = f"https://api.pushshift.io/reddit/search/comment/?subreddit={subreddit}&size={limit}&after={start}d&before={end}d"
    headers = {"Accept": "application/json"}

    try:
        res = requests.get(url, headers=headers)
        json = res.json()
        return json["data"]
    except Exception as e:
        print(f"Extraction of legacy comments error: {e}")
        return []


def get_processed_data(comment: dict, tickers: list) -> Comment:
    body = remove_emojies(comment["body"])
    post_url = comment["permalink"].split("/")
    for word in body.strip().split(" "):
        if word in tickers:
            return Comment(
                comment["permalink"],
                word,
                "/".join(post_url[:-2]),
                comment["subreddit"],
                comment["utc_datetime_str"],
                comment["score"],
                body,
                comment["author"],
            )
