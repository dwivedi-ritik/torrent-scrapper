import os
import csv
from typing import Union, Dict
from dto import TorrentDto

from models import TorrentProvider, db, TorrentProviderCode
from service.torrent_provider_service import get_torrent_provider_by_code

TORRENT_CSV_FILE_PATH = os.environ.get("TORRENT_CSV") or "./torrents.csv"


def add_torrent_from_torrent_csv() -> bool:
    """Method will add csv into"""
    if not os.path.exists(TORRENT_CSV_FILE_PATH):
        return False
    provider: Union[TorrentProvider, None] = get_torrent_provider_by_code(
        TorrentProviderCode.TORRENT_CSV
    )
    if not provider:
        return False
    with open(TORRENT_CSV_FILE_PATH, "r+", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for counter, reader in enumerate(csv_reader):
            dto_dict: Dict = {
                "name": reader["name"],
                "magnetUri": reader["infohash"],
                "seeders": int(reader["seeders"]),
                "leeches": int(reader["leechers"]),
                "torrentProviderId": provider.id,
            }
            torrent_dto = TorrentDto(**dto_dict)
            torrent = torrent_dto.model_instance()
            db.session.merge(torrent)

            if counter % 100 == 0:
                db.session.commit()

            if counter >= 1000:
                break

    return True
