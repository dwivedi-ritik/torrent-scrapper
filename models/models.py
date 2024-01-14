from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

db = SQLAlchemy()


@dataclass
class AddedTorrentProvider:
    id: int
    provider_name: str
    provider_last_updated: str


class TorrentProvider(db.Model):
    """Parent class of torrent"""

    __tablename__ = "torrent_provider"
    id = Column(sqlalchemy.BIGINT, primary_key=True, autoincrement=True)
    provider_name = Column(sqlalchemy.String(100))
    provider_last_updated = Column(sqlalchemy.DateTime(timezone=True))
    torrent = relationship("Torrent", backref="TorrentProvider")

    def to_dto(self) -> AddedTorrentProvider:
        """Return the model into AddedTorrentProvider a DTO"""
        return AddedTorrentProvider(
            **{
                "id": self.id,
                "provider_name": self.provider_name,
                "provider_last_updated": self.provider_last_updated,
            }
        )


class Torrent(db.Model):
    """Model of Torrent"""

    __tablename__ = "torrents"
    id = Column(sqlalchemy.BigInteger, primary_key=True, autoincrement=True)
    name = Column(sqlalchemy.String(1000), nullable=False)
    magnet_uri = Column(sqlalchemy.String(10000), nullable=False)
    imdb_rating = Column(sqlalchemy.DOUBLE_PRECISION())
    imdb_url = Column(sqlalchemy.Text())
    created_at = Column(
        sqlalchemy.DateTime(timezone=True), server_default=func.now()
    )  # pylint: disable=E1102
    torrent_provider_id = Column(
        sqlalchemy.BIGINT, sqlalchemy.ForeignKey("torrent_provider.id")
    )
