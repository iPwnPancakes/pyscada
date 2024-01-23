"""Make MqttConfig table

Revision ID: 99a1b6a6340f
Revises: d9391e31c0f2
Create Date: 2024-01-22 23:41:24.395298

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '99a1b6a6340f'
down_revision: Union[str, None] = 'd9391e31c0f2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'mqtt_configs',
        sa.Column('id', sa.Integer, nullable=False, primary_key=True),
        sa.Column('address', sa.String(255), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('mqtt_configs')
