from bs4 import BeautifulSoup
import requests

WIKI_BASE_URL = "https://en.wikipedia.org"


def get_stars_on_hollywood_walk_of_fame_links():
    """
    Function to fetch links to celebrity sub-pages belonging
    to subsection `stars on hollywood walk of fame`.
    """

    url = WIKI_BASE_URL + "/wiki/List_of_stars_on_the_Hollywood_Walk_of_Fame"

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    div_soup = soup.find("div", id="mw-content-text").div

    total_link_list = list()

    for ndiv_soup in div_soup.find_all("table"):
        if ndiv_soup is not None:
            link_suffix_list = ndiv_soup.find_all("a", href=True)

            link_suffix_list = filter(lambda x: "http" not in x['href'],
                                      link_suffix_list)

            link_list = [WIKI_BASE_URL+link_suffix["href"]
                         for link_suffix in link_suffix_list]

            total_link_list.extend(link_list)

    return list(total_link_list)
