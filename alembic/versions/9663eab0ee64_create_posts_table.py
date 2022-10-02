"""create posts table

Revision ID: 9663eab0ee64
Revises: 
Create Date: 2022-09-18 07:55:02.608688

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9663eab0ee64'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), 
    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
