import os
import csv
from typing import List, Union
from dto import TorrentDto

from models import TorrentProvider, db, TorrentProviderCode
from service.torrent_provider_service import get_torrent_provider_by_code

TORRENT_CSV_FILE_PATH = os.environ.get("TORRENT_CSV") or "../torrents.csv"


def get_torrent_dto_from_torrent_csv() -> List[TorrentDto]:  # TBD
    pass
    # if not os.path.exists(TORRENT_CSV_FILE_PATH): return []
    # torrent_dto_list = []
    # provider:Union[TorrentProvider, None] =  get_torrent_provider_by_code(TorrentProviderCode.TORRENT_CSV)
    # if not provider: return
    # with open(TORRENT_CSV_FILE_PATH, "r+") as csv_file:
    #     csv_reader = csv.DictReader(csv_file)
    #     for reader in csv_file:
    #         torrent_dto = TorrentDto(name=reader['name'], magnetUri=name['infohash'], seeders=readers['seeders'], leeches=reader['leechers'], torrentProviderId= provider.id)
    # return


# class TorrentCSV:
#     def __init__(self):
#         self.torrent_path: str = os.environ.get("TORRENT_CSV") or "../torrents.csv"
#         self.

#     def get_csv_reader(self):
#         with open(self.torrent_path, "r+") as f:
#             dict_reader = csv.DictReader(f)


# infohash,name,size_bytes,created_unix,seeders,leechers,completed,scraped_date,published
