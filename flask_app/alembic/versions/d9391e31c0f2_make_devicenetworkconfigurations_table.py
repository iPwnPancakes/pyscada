"""Make DeviceNetworkConfigurations table

Revision ID: d9391e31c0f2
Revises: 125c59d89d1e
Create Date: 2024-01-20 22:42:49.937240

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'd9391e31c0f2'
down_revision: Union[str, None] = '125c59d89d1e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'device_network_configurations',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False, autoincrement=True),
        sa.Column('device_id', sa.Integer, sa.ForeignKey('devices.id'), nullable=False, unique=True),
        sa.Column('ip_address', sa.String(length=255), nullable=False),
        sa.Column('port', sa.Integer, nullable=False),
    )


def downgrade() -> None:
    op.drop_table('device_network_configurations')
