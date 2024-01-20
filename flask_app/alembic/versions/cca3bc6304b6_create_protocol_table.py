"""Create Protocol table

Revision ID: cca3bc6304b6
Revises: cdb1343276c3
Create Date: 2024-01-14 12:00:27.999209

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cca3bc6304b6'
down_revision: Union[str, None] = 'cdb1343276c3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'protocol',
        sa.Column('id', sa.BIGINT, primary_key=True, nullable=False, autoincrement=True),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('description', sa.TEXT, nullable=False),
    )


def downgrade() -> None:
    op.drop_table('protocol')
