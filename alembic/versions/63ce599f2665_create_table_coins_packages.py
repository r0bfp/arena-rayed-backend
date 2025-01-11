"""create table coins_packages

Revision ID: 63ce599f2665
Revises: 14b8c4f71929
Create Date: 2025-01-06 08:41:47.827773

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '63ce599f2665'
down_revision: Union[str, None] = '14b8c4f71929'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    table = op.create_table(
        'coins_packages',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('amount', sa.Float, nullable=False),
        sa.Column('price', sa.Float, nullable=False)
    )

    op.bulk_insert(
        table,
        [
            {'id': 1, 'amount': 100, 'price': 4.9},
            {'id': 2, 'amount': 200, 'price': 8.9},
            {'id': 3, 'amount': 300, 'price': 12.9},
            {'id': 4, 'amount': 500, 'price': 17.9},
            {'id': 5, 'amount': 750, 'price': 24.9},
            {'id': 6, 'amount': 1000, 'price': 29.9},
        ]
    )


def downgrade() -> None:
    op.drop_table('coins_packages')
