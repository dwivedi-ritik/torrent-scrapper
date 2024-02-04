from typing import List

import requests
from bs4 import BeautifulSoup

from dto import TorrentDto


def get_json(soup):
    table = soup.table
    tables = table.find_all("td")

    json_obj = {"movie_info": []}
    seeders = []
    for el in table.find_all("td"):
        if el.div and el.div.a:
            json_obj["movie_info"].append(
                {
                    "title": el.div.text.strip("\n"),
                    "magnet_url": el.find_all("a")[1]["href"],
                }
            )
        if el.get("align"):
            seeders.append(el.text)

    k = 0
    for i in range(0, len(seeders), 2):
        json_obj["movie_info"][k]["seeders"] = seeders[i]
        json_obj["movie_info"][k]["leeches"] = seeders[i + 1]
        k += 1
    return json_obj


def get_top_pirate_torrent(PIRATE_ID: int) -> List[TorrentDto]:
    """Method returns the top priate bay torrent"""
    TOP_URL = "https://tpb.party/top/all"
    res = requests.get(TOP_URL)
    if res.status_code != 200:
        return []
    soup = BeautifulSoup(res.content, "html.parser")
    raw_torrents_list = get_json(soup)[
        "movie_info"
    ]  # Some values are hardocded to avoid breaking existing methods

    top_pirate: List[TorrentDto] = []
    for torrent in raw_torrents_list:
        torrent_dto = TorrentDto(
            name=torrent["title"],
            magnetUri=torrent["magnet_url"],
            leeches=torrent["leeches"],
            seeders=torrent["seeders"],
            imdbRating=None,
            imdbUrl=None,
            torrentProviderId=PIRATE_ID,
        )
        top_pirate.append(torrent_dto)
    return top_pirate


def pirate(query, top=False):
    if top and query is None:
        url = "https://tpb.party/top/all"
    else:
        url = f"https://tpb.party/search/{query}"
    res = requests.get(url)
    if res.status_code != 200:
        raise ValueError("Ops didn't get valid response")
    content = res.content
    soup = BeautifulSoup(content, "html.parser")
    obj = get_json(soup)
    return obj
