from bs4 import BeautifulSoup
import requests

WIKI_BASE_URL = "https://en.wikipedia.org"


def get_television_presenters_links():
    """
    Function to fetch links to celebrity sub-pages belonging
    to subsection `television presenters`.
    """

    url = WIKI_BASE_URL + "/wiki/List_of_television_presenters"

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    div_soup = soup.find("div", id="mw-content-text").div

    total_link_list = list()

    for idx in range(5, 80):
        css_selector = f"div:nth-child({idx})"
        ndiv_soup = div_soup.select_one(css_selector)

        if ndiv_soup is not None:
            link_suffix_list = ndiv_soup.find_all("a")

            link_suffix_list = filter(
                lambda x: r"http" not in x['href'],
                link_suffix_list)

            link_suffix_list = filter(
                lambda x: r"File" not in x['href'],
                link_suffix_list)

            link_suffix_list = filter(
                lambda x: r"Wikipedia" not in x['href'],
                link_suffix_list)

            link_list = [WIKI_BASE_URL+link_suffix["href"]
                         for link_suffix in link_suffix_list]

            total_link_list.extend(link_list)

    return list(filter(lambda x: r'Template' not in x, total_link_list))


def get_television_presenters_links2():
    """
    Function to fetch links to celebrity sub-pages belonging
    to subsection `television presenters`.
    """

    url = WIKI_BASE_URL + "/wiki/List_of_television_presenters"

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    div_soup = soup.find("div", id="mw-content-text").div

    total_link_list = list()

    for idx in range(5, 80):
        css_selector = f"ul:nth-child({idx})"
        ndiv_soup = div_soup.select_one(css_selector)

        if ndiv_soup is not None:
            link_suffix_list = ndiv_soup.find_all("a")

            link_suffix_list = filter(
                lambda x: r"http" not in x['href'],
                link_suffix_list)

            link_suffix_list = filter(
                lambda x: r"File" not in x['href'],
                link_suffix_list)

            link_suffix_list = filter(
                lambda x: r"Wikipedia" not in x['href'],
                link_suffix_list)

            link_suffix_list = filter(
                lambda x: r"List_of" not in x['href'],
                link_suffix_list)

            link_list = [WIKI_BASE_URL+link_suffix["href"]
                         for link_suffix in link_suffix_list]

            total_link_list.extend(link_list)

    return list(filter(lambda x: r'Template' not in x, total_link_list))