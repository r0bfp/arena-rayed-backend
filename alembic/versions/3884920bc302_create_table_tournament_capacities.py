"""create table tournament_capacities

Revision ID: 3884920bc302
Revises: 767d5433afc4
Create Date: 2024-12-29 19:52:00.990000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3884920bc302'
down_revision: Union[str, None] = '767d5433afc4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    table = op.create_table(
        'tournament_capacities',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('capacity', sa.Integer, nullable=False),
        sa.Column('price', sa.Integer, nullable=False)
    )

    op.bulk_insert(
        table,
        [
            {'id': 1, 'capacity': 4, 'price': 100},
            {'id': 2, 'capacity': 8, 'price': 200},
            {'id': 3, 'capacity': 16, 'price': 300},
            {'id': 4, 'capacity': 32, 'price': 400},
            {'id': 5, 'capacity': 64, 'price': 500},
            {'id': 6, 'capacity': 128, 'price': 600},
        ]
    )


def downgrade() -> None:
    op.drop_table('tournament_capacities')
