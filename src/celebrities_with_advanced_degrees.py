from bs4 import BeautifulSoup
import requests

WIKI_BASE_URL = "https://en.wikipedia.org/"

def get_celebrity_links():
    """
    Function to fetch links to celebrity sub-pages belonging
    to subsection `celibrities with advanced degrees.
    """

    url = WIKI_BASE_URL + "/wiki/List_of_celebrities_with_advanced_degrees"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    css_selector = '#mw-content-text > div > table > tbody > tr > td:nth-child(1)'
    link_suffix_list = soup.select(css_selector)

    # print(link_suffix_list)

    link_list = [WIKI_BASE_URL+link_suffix.find("a")["href"]
                 for link_suffix in link_suffix_list]

    return link_list