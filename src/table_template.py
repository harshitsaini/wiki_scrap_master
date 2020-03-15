from bs4 import BeautifulSoup
import requests

WIKI_BASE_URL = "https://en.wikipedia.org/"

def get_guest_star_links():
    """
    Function to fetch links to celebrity sub-pages belonging
    to subsection guest stars of The Simpsons.
    """

    url = WIKI_BASE_URL + "/wiki/List_of_The_Simpsons_guest_stars"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    css_selector = '#mw-content-text > div > table:nth-child(54) > tbody > tr > th'
    link_suffix_list = soup.select(css_selector)[6:]

    link_list = [WIKI_BASE_URL+link_suffix.find("a")["href"]
                 for link_suffix in link_suffix_list]

    return link_list