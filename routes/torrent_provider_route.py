from dataclasses import dataclass, asdict, field
from typing import Union
from sqlalchemy.sql import func
from flask import Blueprint, request, jsonify
from models import TorrentProvider, db, AddedTorrentProvider


@dataclass
class TorrentProviderDto:
    provider_name: str
    provider_last_updated: Union[str, None] = field(default=None)


torrent_provider_blueprint = Blueprint("torrent_provider", __name__)


@torrent_provider_blueprint.route("/getAll", methods=["GET"])
def fetch_all_torrent_provider():
    torrent_provider = TorrentProvider()
    return jsonify(torrent_provider.query.all())


@torrent_provider_blueprint.route("/add", methods=["POST"])
def add_torrent_provider():
    torrent_provider_dto = TorrentProviderDto(**request.json)  # type: ignore

    torrent_provider_dto.provider_last_updated = func.now()

    torrent_provider = TorrentProvider(**asdict(torrent_provider_dto))
    db.session.add(torrent_provider)
    db.session.flush()

    db.session.commit()

    torrent_provider_dto = torrent_provider.to_dto()
    return jsonify(asdict(torrent_provider_dto))
