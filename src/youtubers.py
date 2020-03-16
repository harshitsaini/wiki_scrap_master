from bs4 import BeautifulSoup
import requests

WIKI_BASE_URL = "https://en.wikipedia.org"


def get_youtubers_links():
    """
    Function to fetch links to celebrity sub-pages belonging
    to subsection `youtubers`.
    """

    url = WIKI_BASE_URL + "/wiki/List_of_YouTubers"

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    div_soup = soup.find("div", id="mw-content-text").div.table.tbody

    th_soup = div_soup.find_all("th", scope='row')

    total_link_list = list()

    for ndiv_soup in th_soup:
        link_suffix_list = ndiv_soup.find_all("a", href=True)
        link_list = [WIKI_BASE_URL+link_suffix["href"]
                     for link_suffix in link_suffix_list]

        total_link_list.extend(link_list)

    return list(filter(lambda x: r'Template' not in x, total_link_list))
