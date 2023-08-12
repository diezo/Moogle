import requests
from requests import Response
from urllib.parse import quote_plus, unquote_plus
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import parse_qs
from .DataStructures import SearchResult


class Search:
    def __new__(cls, *args, **kwargs) -> list[SearchResult]:
        if len(args) != 1: raise Exception("Pass only search query as an argument!")

        encoded_query = "+".join([quote_plus(key) for key in args[0].strip().split(" ")])
        response: Response = requests.get(f"https://google.com/search?q={encoded_query}")

        soup = BeautifulSoup(response.text, features="html.parser")

        objects = soup.find_all("div", {"class": "Gx5Zad fP1Qef xpd EtOod pkphOe"})
        results: list[SearchResult] = []

        for each in objects:
            title = each.find_next().find_next().find_next().find_next().find_next().find_next().text
            destination = unquote_plus(
                parse_qs(urlparse(each.find_next().find_next().get("href")).query).get("q", "")[0])

            results.append(SearchResult(title, destination))

        return results
