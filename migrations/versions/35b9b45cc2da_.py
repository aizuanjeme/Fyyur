"""empty message

Revision ID: 35b9b45cc2da
Revises: 945ceb797e98
Create Date: 2022-05-20 11:59:44.786612

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35b9b45cc2da'
down_revision = '945ceb797e98'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venue', sa.Column('website_link', sa.String(length=120), nullable=True))
    op.drop_column('venue', 'website')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venue', sa.Column('website', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_column('venue', 'website_link')
    # ### end Alembic commands ###
