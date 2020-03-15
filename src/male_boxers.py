from bs4 import BeautifulSoup
import requests

WIKI_BASE_URL = "https://en.wikipedia.org/"

def get_male_boxers_links():
    """
    Function to fetch links to celebrity sub-pages belonging
    to subsection `female boxers`.
    """

    url = WIKI_BASE_URL + "/wiki/List_of_male_boxers"

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    div_soup = soup.find("div", id="mw-content-text").div

    total_link_list = list()

    for idx in range(5, 60):
        css_selector = f"div:nth-child({idx})"
        ndiv_soup = div_soup.select_one(css_selector)

        if ndiv_soup is not None:
            link_suffix_list = ndiv_soup.find_all("a")

            link_list = [WIKI_BASE_URL+link_suffix["href"]
                         for link_suffix in link_suffix_list]

            total_link_list.extend(link_list)

    return total_link_list
