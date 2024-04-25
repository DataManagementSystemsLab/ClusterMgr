"""empty message

Revision ID: f1be5a466948
Revises: b7e7a9d26f5d
Create Date: 2024-02-19 02:37:18.844096

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1be5a466948'
down_revision = 'b7e7a9d26f5d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=128), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=4096), nullable=True),
    sa.Column('posted', sa.DateTime(), nullable=True),
    sa.Column('commenter_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['commenter_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    op.drop_table('users')
    # ### end Alembic commands ###