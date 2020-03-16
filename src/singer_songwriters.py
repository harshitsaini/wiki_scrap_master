import sys
import itertools
from functools import reduce
from multiprocessing.pool import Pool

from bs4 import BeautifulSoup
import requests

WIKI_BASE_URL = "https://en.wikipedia.org"


def join_lists(x, y):
    x.extend(y)
    return x


def link_fetch_lambda(idx, soup):

    css_selector = f'div:nth-child({idx}) > ul'
    div_select = soup.select_one(css_selector)
    if div_select is not None:
        link_suffix_list = div_select.find_all('a', href=True)
    else:
        link_suffix_list = list()

    link_list = [WIKI_BASE_URL+link_suffix["href"]
                 for link_suffix in link_suffix_list]

    if link_list is None:
        return list()

    return link_list


def get_singer_songwriters_links():
    """
    Function to fetch links to celebrity sub-pages belonging
    to subsection `singer songwriters`.
    """

    url = WIKI_BASE_URL + "/wiki/List_of_singer-songwriters"

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    div_soup = soup.find("div", id="mw-content-text").div

    pool = Pool(4)

    sys.setrecursionlimit(99999)

    arg_list = list(zip(range(5, 233),
                        itertools.repeat(div_soup)))

    total_link_list_shredded = pool.starmap(link_fetch_lambda,
                                            arg_list)

    total_link_list = list(reduce(lambda x, y: join_lists(x, y),
                                  total_link_list_shredded))

    return list(filter(lambda x: r'Template' not in x,
                       total_link_list))


def link_fetch_lambda2(idx, soup):

    css_selector = f'ul:nth-child({idx})'
    div_select = soup.select_one(css_selector)
    if div_select is not None:
        link_suffix_list = div_select.find_all('a', href=True)
    else:
        link_suffix_list = list()

    link_list = [WIKI_BASE_URL+link_suffix["href"]
                 for link_suffix in link_suffix_list]

    if link_list is None:
        return list()

    return link_list


def get_singer_songwriters_links2():
    """
    Function to fetch links to celebrity sub-pages belonging
    to subsection `singer songwriters`.
    """

    url = WIKI_BASE_URL + "/wiki/List_of_singer-songwriters"

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    div_soup = soup.find("div", id="mw-content-text").div

    pool = Pool(4)

    sys.setrecursionlimit(99999)

    arg_list = list(zip(range(5, 233),
                        itertools.repeat(div_soup)))

    total_link_list_shredded = pool.starmap(link_fetch_lambda2,
                                            arg_list)

    total_link_list = list(reduce(lambda x, y: join_lists(x, y),
                                  total_link_list_shredded))

    return list(filter(lambda x: r'Template' not in x,
                       total_link_list))