"""Add device_id column to Tags table

Revision ID: 125c59d89d1e
Revises: 94e0977187fd
Create Date: 2024-01-14 14:04:03.550307

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '125c59d89d1e'
down_revision: Union[str, None] = '94e0977187fd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table('tags') as batch_op:
        batch_op.add_column(
            sa.Column(
                'device_id',
                sa.BIGINT,
                sa.ForeignKey('devices.id', name='fk_tags_device_id'),
                nullable=False
            )
        )


def downgrade() -> None:
    op.drop_column('tags', 'device_id')
