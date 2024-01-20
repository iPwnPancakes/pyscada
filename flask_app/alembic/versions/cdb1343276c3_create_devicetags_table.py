"""Create DeviceTags table

Revision ID: cdb1343276c3
Revises: 6d51231580a2
Create Date: 2024-01-14 11:24:56.282703

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cdb1343276c3'
down_revision: Union[str, None] = '6d51231580a2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'device_tags',
        sa.Column('id', sa.BIGINT, primary_key=True, nullable=False, autoincrement=True),
        sa.Column('device_id', sa.INTEGER, sa.ForeignKey('devices.id'), nullable=False),
        sa.Column('tag_id', sa.INTEGER, sa.ForeignKey('tags.id'), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('device_tags')
