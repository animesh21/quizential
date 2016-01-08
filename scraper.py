import requests
from bs4 import BeautifulSoup


def get_feeds(url="http://www.sciencedaily.com/"):
    """
    gets the rss feed links of the website at the given url
    :param url: url of the website from where feed links to be parsed
    :return: list of rss feed urls
    """

    res = requests.get(url)
    print(res.status_code)
    soup = BeautifulSoup(res.text, "html.parser")
    print(soup.prettify())
    links = soup.find_all("a")
    for link in links:
        print(link)
