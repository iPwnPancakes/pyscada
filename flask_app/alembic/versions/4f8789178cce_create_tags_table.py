"""create tags table

Revision ID: 4f8789178cce
Revises: 
Create Date: 2024-01-13 22:41:43.421295

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4f8789178cce'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'tags',
        sa.Column('id', sa.BIGINT, primary_key=True, nullable=False),
        sa.Column('name', sa.String(255), nullable=True),
        sa.Column('value_int', sa.INTEGER, nullable=True),
        sa.Column('value_float', sa.FLOAT, nullable=True),
        sa.Column('value_bool', sa.BOOLEAN, nullable=True),
        sa.Column('value_string', sa.String(255), nullable=True),
    )


def downgrade() -> None:
    op.drop_table('tags')
