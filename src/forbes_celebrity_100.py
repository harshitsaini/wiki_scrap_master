#mw-content-text > div > table:nth-child(8) > tbody > tr:nth-child(2) > td:nth-child(2) > a
#mw-content-text > div > table:nth-child(8) > tbody > tr:nth-child(9) > td:nth-child(2) > a

#mw-content-text > div > table:nth-child(10) > tbody > tr:nth-child(9) > td:nth-child(2) > a

#mw-content-text > div > table:nth-child(11) > tbody > tr:nth-child(7) > td:nth-child(2) > a

#mw-content-text > div > table:nth-child(12) > tbody > tr:nth-child(7) > td:nth-child(2) > a

#mw-content-text > div > table:nth-child(13) > tbody > tr:nth-child(6) > td:nth-child(2) > a

#mw-content-text > div > table:nth-child(14) > tbody > tr:nth-child(11) > td:nth-child(2) > a

#mw-content-text > div > table:nth-child(28) > tbody > tr:nth-child(10) > td:nth-child(2) > a

#mw-content-text > div > table:nth-child(30) > tbody > tr:nth-child(6) > td:nth-child(2) > a

#mw-content-text > div > table:nth-child(30) > tbody > tr:nth-child(6) > td:nth-child(2) > a

from bs4 import BeautifulSoup
import requests

WIKI_BASE_URL = "https://en.wikipedia.org/"


def get_forbes_celebrity_100_links():
    """
    Function to fetch links to celebrity sub-pages belonging
    to subsection `forbes celebrity 100`.
    """

    url = WIKI_BASE_URL + "/wiki/Forbes_Celebrity_100"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    div_soup = soup.find("div", id="mw-content-text").div

    total_linked_list = list()

    for idx in range(8, 31):
        css_selector = f'table:nth-child({idx})'
        table_soup = soup.select_one(css_selector)

        if table_soup is not None:
            link_suffix_list = table_soup.tbody.select("tr > td:nth-child(2) > a")

            link_list = [WIKI_BASE_URL+link_suffix["href"]
                         for link_suffix in link_suffix_list]

            total_linked_list.extend(link_list)

    return total_linked_list
