"""Create DeviceTagConfig table

Revision ID: 8e21e0ef8d37
Revises: cca3bc6304b6
Create Date: 2024-01-14 12:02:12.768685

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8e21e0ef8d37'
down_revision: Union[str, None] = 'cca3bc6304b6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'device_tag_config',
        sa.Column('id', sa.BIGINT, primary_key=True, nullable=False),
        sa.Column('device_id', sa.INTEGER, sa.ForeignKey('devices.id'), nullable=False),
        sa.Column('tag_id', sa.INTEGER, sa.ForeignKey('tags.id'), nullable=False),

        # Polymorphic association
        sa.Column('protocol_type', sa.INTEGER, nullable=False),
        sa.Column('protocol_config_id', sa.INTEGER, nullable=False),
    )


def downgrade() -> None:
    op.drop_table('device_tag_config')
