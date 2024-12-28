"""create table users_tournaments

Revision ID: a8a7b5a98ec2
Revises: 637578f2e072
Create Date: 2024-12-27 21:06:23.973605

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a8a7b5a98ec2'
down_revision: Union[str, None] = '637578f2e072'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users_tournaments',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, nullable=False),
        sa.Column('tournament_id', sa.Integer, nullable=False),
    )


def downgrade() -> None:
    op.drop_table('users_tournaments')
