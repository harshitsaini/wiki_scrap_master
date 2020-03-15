import requests
from bs4 import BeautifulSoup

WIKI_BASE_URL = "https://en.wikipedia.org/"


def get_league_of_legends_players_links():
    """
    Function to fetch links to celebrity sub-pages belonging
    to subsection `league of legends players`.
    """

    url = WIKI_BASE_URL + "/wiki/Category:League_of_Legends_players"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    div_soup = soup.find("div", id="mw-pages").div.div

    total_link_list = list()

    for idx in range(1, 26):
        css_selector = f"div:nth-child({idx})"
        link_suffix_list = div_soup.select_one(css_selector).ul.find_all("a")

        link_list = [WIKI_BASE_URL+link_suffix["href"]
                     for link_suffix in link_suffix_list]

        total_link_list.extend(link_list)

    return total_link_list
