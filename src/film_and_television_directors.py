import sys
import itertools
from functools import reduce
from multiprocessing.pool import Pool

import requests
from bs4 import BeautifulSoup, SoupStrainer

WIKI_BASE_URL = "https://en.wikipedia.org/"


def join_lists(x, y):
    x.extend(y)
    return x


def link_fetch_lambda(idx, soup):

    css_selector = f'div:nth-child({idx})'
    div_select = soup.select_one(css_selector)
    if div_select is not None:
        link_suffix_list = div_select.find_all('a')
    else:
        link_suffix_list = list()

    link_list = [WIKI_BASE_URL+link_suffix["href"]
                 for link_suffix in link_suffix_list]

    if link_list is None:
        return list()

    return link_list


def get_film_and_television_directors_links():
    """
    Function to fetch links to celebrity sub-pages belonging
    to subsection `film and television directors`.
    """

    url = WIKI_BASE_URL + "/wiki/List_of_film_and_television_directors"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    div_soup = soup.find("div", id="mw-content-text").div

    pool = Pool(4)

    sys.setrecursionlimit(99999)

    arg_list = list(zip(range(6, 93),
                        itertools.repeat(div_soup)))

    total_link_list_shredded = pool.starmap(link_fetch_lambda,
                                            arg_list)

    total_link_list = list(reduce(lambda x, y: join_lists(x, y),
                                  total_link_list_shredded))

    return total_link_list