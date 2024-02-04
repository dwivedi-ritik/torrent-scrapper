from models import db
from dto import TorrentDto
from lib.piratebay import get_top_pirate_torrent


def add_torrent_in_db(torrent_dto: TorrentDto) -> bool:
    """Takes torrent dto and add intro torrent table"""
    torrent = torrent_dto.model_instance()
    db.session.add(torrent)
    db.session.commit()
    return True


def add_top_pirate_in_db() -> bool:
    pirate_list = get_top_pirate_torrent(1)
    for pirate in pirate_list:
        add_torrent_in_db(pirate)
    return True
