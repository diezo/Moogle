import requests
from requests import Response
from urllib.parse import quote_plus, unquote_plus
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import parse_qs
from .DataStructures import SearchResult


# noinspection PyTypeChecker, PyPep8Naming
def Search(query: str, page: int = 1) -> list[SearchResult]:
    """
    Searches for given query on Google and returns list of results.
    Each page contains maximum 9 search results.

    :rtype: SearchResult
    :param query:
    :param page:
    :return:
    """

    results: list[SearchResult] = []
    encoded_query = "+".join([quote_plus(key) for key in query.strip().split(" ")])

    start = "" if page < 2 else f"&start={page * 10 - 10}"
    response: Response = requests.get(f"https://google.com/search?q={encoded_query}{start}")

    soup = BeautifulSoup(response.text, features="html.parser")
    objects = soup.find_all("div", {"class": "Gx5Zad fP1Qef xpd EtOod pkphOe"})

    for each in objects:
        title = each.find_next().find_next().find_next().find_next().find_next().find_next().text
        description = each.find_next().next_sibling.find_next().find_next().find_next().find_next().find_next().text
        destination = unquote_plus(parse_qs(urlparse(each.find_next().find_next().get("href")).query).get("q", "")[0])

        results.append(SearchResult(title, description, destination))

    return results
