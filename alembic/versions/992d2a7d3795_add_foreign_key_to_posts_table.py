"""add foreign-key to posts table

Revision ID: 992d2a7d3795
Revises: c63042bebdd1
Create Date: 2022-09-18 08:54:41.137681

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '992d2a7d3795'
down_revision = 'c63042bebdd1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
