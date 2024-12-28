"""create table games

Revision ID: f21be373ad15
Revises: a8a7b5a98ec2
Create Date: 2024-12-27 21:19:06.242534

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f21be373ad15'
down_revision: Union[str, None] = 'a8a7b5a98ec2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'games',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(length=50), nullable=False),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime),
    )


def downgrade() -> None:
    op.drop_table('games')
