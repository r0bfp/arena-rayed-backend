"""create table users

Revision ID: e017a6443730
Revises: 
Create Date: 2024-12-27 20:27:52.694248

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e017a6443730'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(length=100), nullable=False),
        sa.Column('password', sa.String(length=200), nullable=False),
        sa.Column('email', sa.String(length=200), nullable=False),
        sa.Column('coins', sa.Integer, nullable=False),
        sa.Column('points', sa.Integer, nullable=False),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime),
    )


def downgrade() -> None:
    op.drop_table('users')
