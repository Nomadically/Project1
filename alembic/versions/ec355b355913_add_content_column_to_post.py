"""add content column to post

Revision ID: ec355b355913
Revises: 9663eab0ee64
Create Date: 2022-09-18 08:06:36.338674

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec355b355913'
down_revision = '9663eab0ee64'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", 'content')
    pass
