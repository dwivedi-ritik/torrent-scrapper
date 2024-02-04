from dataclasses import dataclass, field
from typing import Any, Union, Type

from models import TorrentProvider


@dataclass
class TorrentProviderDto:
    """DTO for Torrent Provider"""

    providerName: str
    code: str
    providerLastUpdated: Union[Any, None] = field(default=None)

    def model_instance(self) -> TorrentProvider:
        """This method will return the instance of Torrent Provider"""
        return TorrentProvider(
            code=self.code,
            provider_name=self.providerName,
            provider_last_updated=self.providerLastUpdated,
        )

    @staticmethod
    def create_instance(
        torrent_provider: TorrentProvider,
    ) -> Type["TorrentProviderDto"]:
        return TorrentProviderDto(
            code=torrent_provider.code.value,  # type: ignore
            providerName=torrent_provider.provider_name,  # type: ignore
            providerLastUpdated=torrent_provider.provider_last_updated,
        )  # type:ignore


@dataclass
class TorrentProviderRefresh:
    """DTO for provider refresh"""

    code: str
