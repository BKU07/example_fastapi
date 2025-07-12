"""add last columns to posts table

Revision ID: 9cc1b1f2b4e0
Revises: 18271e4f3954
Create Date: 2025-07-10 18:27:23.410001

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9cc1b1f2b4e0'
down_revision: Union[str, Sequence[str], None] = '18271e4f3954'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() :
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))
    op.add_column('posts', sa.Column('published', sa.Boolean(), server_default='TRUE', nullable=False))

    pass


def downgrade() :
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
