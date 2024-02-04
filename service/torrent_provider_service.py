from typing import Union
from models import TorrentProvider, TorrentProviderCode, db
from dto import TorrentProviderDto


def get_torrent_provider_dto_by_code(
    code: TorrentProviderCode,
) -> Union[TorrentProviderDto, None]:
    """Return the TorrentProviderDto by code"""
    fetched_provider: Union[TorrentProvider, None] = db.session.query(TorrentProvider).filter(TorrentProvider.code == code.value).first()  # type: ignore
    if fetched_provider:
        torrent_provider_dto: TorrentProviderDto = TorrentProviderDto.create_instance(fetched_provider)  # type: ignore
        return torrent_provider_dto
    return None


def get_torrent_provider_by_code(
    code: TorrentProviderCode,
) -> Union[TorrentProvider, None]:
    """Return the TorrentProviderDto by code"""
    fetched_provider: Union[TorrentProvider, None] = db.session.query(TorrentProvider).filter(TorrentProvider.code == code.value).first()  # type: ignore
    if fetched_provider:
        return fetched_provider
    return None
