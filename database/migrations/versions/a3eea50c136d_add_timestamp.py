"""add timestamp

Revision ID: a3eea50c136d
Revises: 
Create Date: 2020-12-19 20:30:13.955464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a3eea50c136d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('note', sa.Column('timestamp', sa.TIMESTAMP(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('note', 'timestamp')
    # ### end Alembic commands ###
