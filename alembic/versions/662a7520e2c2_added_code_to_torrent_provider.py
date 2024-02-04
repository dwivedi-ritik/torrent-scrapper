"""Added code to torrent provider

Revision ID: 662a7520e2c2
Revises: 
Create Date: 2024-02-04 11:29:40.329020

"""

from typing import Sequence, Union
from enum import Enum
from alembic import op
import sqlalchemy as sa


class TorrentProviderCode(Enum):
    """Enum of Torrent Porvider code"""

    PIRATE = "PIRATE"
    TORRENT_CSV = "TORRENT_CSV"


# revision identifiers, used by Alembic.
revision: str = "662a7520e2c2"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE TYPE code AS ENUM ('PIRATE', 'TORRENT_CSV')")
    op.add_column(
        "torrent_provider", sa.Column("code", sa.Enum(TorrentProviderCode, name="code"))
    )


def downgrade() -> None:
    pass
