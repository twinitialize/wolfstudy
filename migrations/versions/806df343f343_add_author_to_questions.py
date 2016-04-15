"""Add author to questions

Revision ID: 806df343f343
Revises: 06422d2e403e
Create Date: 2016-04-11 21:05:34.651267

"""

# revision identifiers, used by Alembic.
revision = '806df343f343'
down_revision = '06422d2e403e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('questions', sa.Column('author_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'questions', 'users', ['author_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'questions', type_='foreignkey')
    op.drop_column('questions', 'author_id')
    ### end Alembic commands ###
