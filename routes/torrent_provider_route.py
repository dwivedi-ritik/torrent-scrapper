from dataclasses import asdict
from typing import Dict, Union
from sqlalchemy.sql import func
from flask import Blueprint, request, jsonify

from models import db, TorrentProvider, TorrentProviderCode
from dto import TorrentProviderDto, TorrentProviderRefresh
from lib.torrentCsv import add_torrent_from_torrent_csv
from service.torrent_service import add_top_pirate_in_db
from service.torrent_provider_service import get_torrent_provider_dto_by_code


torrent_provider_blueprint = Blueprint("torrent_provider", __name__)


@torrent_provider_blueprint.route("/getAll", methods=["GET"])
def fetch_all_torrent_provider():
    """Get all torrent provider"""
    torrent_provider_list = db.session().query(TorrentProvider).all()  # type: ignore

    return jsonify(
        [
            asdict(TorrentProviderDto.create_instance(torrent_provider))
            for torrent_provider in torrent_provider_list
        ]
    )


@torrent_provider_blueprint.route("/get", methods=["GET"])  # type: ignore
def get_torrent_provider_by_params():
    """Get torrent provider by params"""
    params: Dict[str, str] = request.args.to_dict()
    if params.get("code") is not None:
        code: str = params.get("code") or ""
        torrent_provider_dto: Union[TorrentProviderDto, None] = None
        if code == TorrentProviderCode.PIRATE.value:
            torrent_provider_dto = get_torrent_provider_dto_by_code(
                TorrentProviderCode.PIRATE
            )
        elif code == TorrentProviderCode.TORRENT_CSV.value:
            torrent_provider_dto = get_torrent_provider_dto_by_code(
                TorrentProviderCode.TORRENT_CSV
            )

        if torrent_provider_dto:
            return jsonify(asdict(torrent_provider_dto))
    return "Not Found"


@torrent_provider_blueprint.route("/add", methods=["POST"])
def add_torrent_provider():
    """Add the torrent provider in DB"""
    torrent_provider_dto = TorrentProviderDto(**request.json)  # type: ignore
    # pylint: disable=not-callable
    torrent_provider_dto.provider_last_updated = func.now()  # type: ignore
    torrent_provider = torrent_provider_dto.model_instance()
    db.session.add(torrent_provider)
    db.session.flush()

    db.session.commit()

    return jsonify(asdict(torrent_provider_dto))


@torrent_provider_blueprint.route("/refresh", methods=["POST"])  # type: ignore
def refresh_pirate_bay():
    """Update the DB with passed torrent client"""
    body = request.get_json()
    current_dto = TorrentProviderRefresh(**body)
    if current_dto.code == TorrentProviderCode.PIRATE.value:

        return add_top_pirate_in_db() and "Pirate updated"
    elif current_dto.code == TorrentProviderCode.TORRENT_CSV.value:
        add_torrent_from_torrent_csv()
        return "Torrent CSV updated"
    return "failed"
