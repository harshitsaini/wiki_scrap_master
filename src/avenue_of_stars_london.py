from bs4 import BeautifulSoup
import requests

WIKI_BASE_URL = "https://en.wikipedia.org"


def get_avenue_of_stars_london_links():
    """
    Function to fetch links to celebrity sub-pages belonging
    to subsection `avenue of stars, london`.
    """

    url = WIKI_BASE_URL + "/wiki/Avenue_of_Stars,_London"

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    div_soup = soup.find("div", id="mw-content-text").div

    css_selector = "table:nth-child(6) > tbody > tr > td:nth-child(1) > ul"
    ndiv_soup = div_soup.select_one(css_selector)

    total_link_list = list()

    if ndiv_soup is not None:
        link_suffix_list = ndiv_soup.find_all("a", href=True)

        link_list = [WIKI_BASE_URL+link_suffix["href"]
                     for link_suffix in link_suffix_list]

        total_link_list.extend(link_list)

    return list(filter(lambda x: r'Template' not in x, total_link_list))
