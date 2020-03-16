from bs4 import BeautifulSoup
import requests

WIKI_BASE_URL = "https://en.wikipedia.org"

# mw-content-text > div > ul:nth-child(5) > li > a
# mw-content-text > div > ul:nth-child(9) > li:nth-child(3) > a
# mw-content-text > div > ul:nth-child(25) > li:nth-child(8) > a
# mw-content-text > div > ul:nth-child(29) > li:nth-child(3) > a


def get_bullfighters_links():
    """
    Function to fetch links to celebrity sub-pages belonging
    to subsection `bullfighters`.
    """

    url = WIKI_BASE_URL + "/wiki/List_of_bullfighters"

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    div_soup = soup.find("div", id="mw-content-text").div

    total_link_list = list()

    for idx in range(5, 30):
        css_selector = f"ul:nth-child({idx})"
        ndiv_soup = div_soup.select_one(css_selector)

        if ndiv_soup is not None:
            link_suffix_list = ndiv_soup.find_all("a", href=True)

            link_suffix_list = filter(lambda x: "http" not in x['href'],
                                      link_suffix_list)

            link_list = [WIKI_BASE_URL+link_suffix["href"]
                         for link_suffix in link_suffix_list]

            total_link_list.extend(link_list)

    return list(total_link_list)
