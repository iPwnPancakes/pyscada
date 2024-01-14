"""Create Devices table

Revision ID: 6d51231580a2
Revises: 4f8789178cce
Create Date: 2024-01-14 11:24:06.040315

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6d51231580a2'
down_revision: Union[str, None] = '4f8789178cce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'devices',
        sa.Column('id', sa.BIGINT, nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('devices')
