"""create table games_tournaments

Revision ID: a7af18884e23
Revises: f21be373ad15
Create Date: 2024-12-27 21:20:39.450287

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a7af18884e23'
down_revision: Union[str, None] = 'f21be373ad15'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'games_tournaments',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('game_id', sa.Integer, nullable=False),
        sa.Column('tournament_id', sa.Integer, nullable=False),
    )


def downgrade() -> None:
    op.drop_table('games_tournaments')
