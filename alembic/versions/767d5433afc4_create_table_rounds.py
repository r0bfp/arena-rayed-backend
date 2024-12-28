"""create table rounds

Revision ID: 767d5433afc4
Revises: a7af18884e23
Create Date: 2024-12-28 20:06:34.529829

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '767d5433afc4'
down_revision: Union[str, None] = 'a7af18884e23'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'rounds',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('player_one_id', sa.Integer, nullable=False),
        sa.Column('player_two_id', sa.Integer, nullable=False),
        sa.Column('tournament_id', sa.Integer, nullable=False),
        sa.Column('winner_id', sa.Integer),
    )


def downgrade() -> None:
    op.drop_table('rounds')
