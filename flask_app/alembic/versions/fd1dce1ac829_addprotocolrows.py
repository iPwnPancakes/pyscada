"""AddProtocolRows

Revision ID: fd1dce1ac829
Revises: 99a1b6a6340f
Create Date: 2024-02-03 16:50:58.026938

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy import table, Column

# revision identifiers, used by Alembic.
revision: str = 'fd1dce1ac829'
down_revision: Union[str, None] = '99a1b6a6340f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    protocol_table = table(
        'protocol',
        Column('id', sa.Integer),
        Column('name', sa.String),
        Column('description', sa.String),
    )

    op.bulk_insert(protocol_table, [
        {'id': 1, 'name': 'Modbus', 'description': 'Modbus protocol'},
        {'id': 2, 'name': 'MQTT', 'description': 'MQTT protocol'},
    ])


def downgrade() -> None:
    op.execute('DELETE FROM protocol WHERE name = "Modbus" OR name = "MQTT"')
