from bs4 import BeautifulSoup
import requests

WIKI_BASE_URL = "https://en.wikipedia.org/"


def get_nationality_links():
    """
    Function to fetch links to celebrity sub-pages belonging
    to subsection nationality.
    """

    url = "https://en.wikipedia.org/wiki/Lists_of_actors"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    link_suffix_list = soup.select(
        '#mw-content-text > div > div:nth-child(8) > ul > li')

    link_list = [WIKI_BASE_URL+link_suffix.find("a")["href"]
                 for link_suffix in link_suffix_list]

    return link_list


def get_specific_roles_or_genres_links():
    """
    Function to fetch links to celebrity sub-pages belonging
    to subsection specific_roles_or_genres.
    """

    url = "https://en.wikipedia.org/wiki/Lists_of_actors"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    link_suffix_list = soup.select(
        '#mw-content-text > div > div:nth-child(5) > ul > li')

    link_list = [WIKI_BASE_URL+link_suffix.find("a")["href"]
                 for link_suffix in link_suffix_list]

    return link_list




def nationality_data():
    ...


def specific_roles_or_genres_data():
    ...