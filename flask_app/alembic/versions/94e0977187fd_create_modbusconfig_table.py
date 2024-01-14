"""Create ModbusConfig table

Revision ID: 94e0977187fd
Revises: 8e21e0ef8d37
Create Date: 2024-01-14 12:04:17.244702

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '94e0977187fd'
down_revision: Union[str, None] = '8e21e0ef8d37'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'modbus_config',
        sa.Column('id', sa.BIGINT, primary_key=True, nullable=False),
        sa.Column('slave_id', sa.INTEGER, nullable=False),
        sa.Column('register', sa.INTEGER, nullable=False),
    )


def downgrade() -> None:
    op.drop_table('modbus_config')
