from dataclasses import asdict
from typing import List, Dict, Type
from flask import Blueprint, jsonify, request
from models import Torrent
from models import db

from dto import TorrentDto

torr_blueprint = Blueprint("torrent_blueprint", __name__)


@torr_blueprint.route("/getAll", methods=["GET"])
def fetch_top_torrents():
    """Fetch all top torrents"""
    all_torrents: List[Torrent] = Torrent.query.all()
    all_torrents_dto: List[Dict] = []
    for torrent in all_torrents:
        torrent_dto: Type["TorrentDto"] = TorrentDto.create_instance(torrent)
        all_torrents_dto.append(asdict(torrent_dto))
    return jsonify(all_torrents_dto)


@torr_blueprint.route("/add", methods=["POST"])
def add_top_torrent():
    """Add top toreent in table"""
    torrent_dto = TorrentDto(**request.json)  # type: ignore
    torrent = torrent_dto.model_instance()
    db.session.add(torrent)
    db.session.commit()
    return jsonify(asdict(torrent_dto))
