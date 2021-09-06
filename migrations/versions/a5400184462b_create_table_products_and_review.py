"""create table products and review

Revision ID: a5400184462b
Revises: 
Create Date: 2021-09-06 20:37:20.681180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5400184462b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('asin', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_product_asin'), 'product', ['asin'], unique=True)
    op.create_table('review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('review', sa.Text(), nullable=True),
    sa.Column('asin', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['asin'], ['product.asin'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('review')
    op.drop_index(op.f('ix_product_asin'), table_name='product')
    op.drop_table('product')
    # ### end Alembic commands ###