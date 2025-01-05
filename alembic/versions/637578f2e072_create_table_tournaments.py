"""create table tournaments

Revision ID: 637578f2e072
Revises: e017a6443730
Create Date: 2024-12-27 20:57:14.064652

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '637578f2e072'
down_revision: Union[str, None] = 'e017a6443730'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'tournaments',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(length=50), nullable=False),
        sa.Column('description', sa.String(length=250)),
        sa.Column('starts_in', sa.DateTime, nullable=False),
        sa.Column('ends_in', sa.DateTime, nullable=False),
        sa.Column('status', sa.String(50), nullable=False),
        sa.Column('capacity_id', sa.Integer, nullable=False),
        sa.Column('game_id', sa.Integer, nullable=False),
        sa.Column('owner_id', sa.Integer, nullable=False),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime),
    )


def downgrade() -> None:
    op.drop_table('tournaments')
