"""add a new column topose table

Revision ID: 24b8e2758383
Revises: fade10baaff5
Create Date: 2025-07-10 18:03:19.680767

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '24b8e2758383'
down_revision: Union[str, Sequence[str], None] = 'fade10baaff5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade(): 
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))

    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
