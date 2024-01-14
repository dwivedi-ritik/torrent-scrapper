from dataclasses import dataclass, field, asdict
from typing import Union
from flask import Blueprint, jsonify, request
from models import Torrent
from models import db

torr_blueprint = Blueprint("torrent_blueprint", __name__)


@dataclass
class TorrentDto:
    name: str
    magnet_uri: str
    torrent_provider_id: int
    imdb_rating: Union[float, None] = field(default=None)
    imdb_url: Union[str, None] = field(default=None)


@torr_blueprint.route("/getAll", methods=["GET"])
def fetch_top_torrents():
    """Fetch all top torrents"""
    all_torrents = Torrent.query.all()
    return jsonify(all_torrents)


@torr_blueprint.route("/add", methods=["POST"])
def add_top_torrent():
    """Add top toreent in table"""
    torrent_dto = TorrentDto(**request.json)  # type: ignore
    torrent = Torrent(**asdict(torrent_dto))
    db.session.add(torrent)
    db.session.commit()
    return jsonify(asdict(torrent_dto))
