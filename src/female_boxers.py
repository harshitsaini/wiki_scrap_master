from bs4 import BeautifulSoup
import requests

WIKI_BASE_URL = "https://en.wikipedia.org"


def get_female_boxers_links():
    """
    Function to fetch links to celebrity sub-pages belonging
    to subsection `female boxers`.
    """

    url = WIKI_BASE_URL + "/wiki/List_of_female_boxers"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    div_soup = soup.find("div", id="mw-content-text").div

    total_linked_list = list()

    for idx in range(5, 50, 2):
        css_selector = f'table:nth-child({idx})'
        table_soup = soup.select_one(css_selector).tbody
        link_suffix_list = table_soup.select("tr > td:nth-child(1)")

        link_list = [WIKI_BASE_URL+link_suffix.a["href"]
                     for link_suffix in link_suffix_list]

        total_linked_list.extend(link_list)
    return total_linked_list
