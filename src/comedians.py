from bs4 import BeautifulSoup
import requests

WIKI_BASE_URL = "https://en.wikipedia.org"

def get_comedians_links():
    """
    Function to fetch links to celebrity sub-pages belonging
    to subsection comedians.
    """

    url = WIKI_BASE_URL + "/wiki/List_of_comedians"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    total_link_list = list()

    for idx in range(10, 65, 2):
        css_selector = f'#mw-content-text > div > div:nth-child({idx}) > ul' \
            + ' > li > a:nth-child(1)'
        link_suffix_list = soup.select(css_selector)

        link_list = [WIKI_BASE_URL+link_suffix["href"]
                     for link_suffix in link_suffix_list]

        total_link_list.extend(link_list)

    return total_link_list
