"""create table players

Revision ID: 14b8c4f71929
Revises: 3884920bc302
Create Date: 2025-01-02 13:55:04.854069

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '14b8c4f71929'
down_revision: Union[str, None] = '3884920bc302'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'players',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('match_id', sa.Integer, nullable=False),
        sa.Column('user_id', sa.Integer, nullable=False),
        sa.Column('status', sa.String(50), nullable=False),
        sa.Column('winner_id', sa.Integer),
    )


def downgrade() -> None:
    op.drop_table('players')
