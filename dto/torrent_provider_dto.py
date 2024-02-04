from dataclasses import dataclass, field
from typing import Any, Union, Type

from models import TorrentProvider


@dataclass
class TorrentProviderDto:
    """DTO for Torrent Provider"""

    providerName: str
    providerLastUpdated: Union[Any, None] = field(default=None)

    def model_instance(self) -> TorrentProvider:
        """This method will return the instance of Torrent Provider"""
        return TorrentProvider(
            provider_name=self.providerName,
            provider_last_updated=self.providerLastUpdated,
        )

    @staticmethod
    def create_instance(
        torrent_provider: TorrentProvider,
    ) -> Type["TorrentProviderDto"]:
        return TorrentProviderDto(
            providerName=torrent_provider.provider_name,  # type: ignore
            providerLastUpdated=torrent_provider.provider_last_updated,
        )  # type:ignore
