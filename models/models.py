from typing import Union, Any
from enum import Enum as PyEnum
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


db = SQLAlchemy()


class TorrentProviderCode(PyEnum):
    """Enum of Torrent Porvider code"""

    PIRATE = "PIRATE"
    TORRENT_CSV = "TORRENT_CSV"


class TorrentProvider(db.Model):
    """Parent class of torrent"""

    __tablename__ = "torrent_provider"
    id = Column(sqlalchemy.BIGINT, primary_key=True, autoincrement=True)
    provider_name = Column(sqlalchemy.String(100))
    provider_last_updated = Column(sqlalchemy.DateTime(timezone=True))
    code = Column(sqlalchemy.Enum(TorrentProviderCode))
    torrent = relationship("Torrent", backref="TorrentProvider")

    def __init__(
        self,
        provider_name: Union[str, None] = None,
        provider_last_updated: Any = None,
        torrent=None,
    ) -> None:
        self.provider_name = provider_name
        self.provider_last_updated = provider_last_updated
        self.torrent = torrent


class Torrent(db.Model):
    """Model of Torrent"""

    __tablename__ = "torrents"
    id = Column(sqlalchemy.BigInteger, primary_key=True, autoincrement=True)
    name = Column(sqlalchemy.String(1000), nullable=False)
    magnet_uri = Column(sqlalchemy.String(10000), nullable=False)
    imdb_rating = Column(sqlalchemy.DOUBLE_PRECISION())
    imdb_url = Column(sqlalchemy.Text())
    # pylint: disable=not-callable
    created_at = Column(sqlalchemy.DateTime(timezone=True), server_default=func.now())
    torrent_provider_id = Column(
        sqlalchemy.BIGINT, sqlalchemy.ForeignKey("torrent_provider.id")
    )

    def __init__(
        self,
        name: Union[str, None],
        magnet_uri: Union[str, None] = None,
        imdb_rating: Union[float, None] = None,
        imdb_url: Union[str, None] = None,
    ):
        self.name = name
        self.magnet_uri = magnet_uri
        self.imdb_rating = imdb_rating
        self.imdb_url = imdb_url
