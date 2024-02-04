from dataclasses import dataclass, field
from typing import Union, Type
from models import Torrent


@dataclass
class TorrentDto:
    """Intentionally added camel casing becuase this will be sent as response"""

    name: str
    magnetUri: str
    torrentProviderId: int
    imdbRating: Union[float, None] = field(default=None)
    imdbUrl: Union[str, None] = field(default=None)
    leeches: Union[int, None] = field(default=None)
    seeders: Union[int, None] = field(default=None)

    def model_instance(self) -> Torrent:
        """This method will return Torrent object, if body is invalid it will throw error"""
        return Torrent(
            name=self.name,
            magnet_uri=self.magnetUri,
            imdb_rating=self.imdbRating,
            imdb_url=self.imdbUrl,
        )

    @staticmethod
    def create_instance(torrent: Torrent) -> Type["TorrentDto"]:
        """This method will be used to send the data in response"""
        return TorrentDto(name=torrent.name, magnetUri=torrent.magnet_uri, torrentProviderId=torrent.torrent_provider_id, imdbRating=torrent.imdb_rating, imdbUrl=torrent.imdb_url)  # type: ignore
