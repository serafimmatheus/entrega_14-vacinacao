"""alterando types cpf

Revision ID: c1cfcdbd5dd5
Revises: 
Create Date: 2022-04-05 12:07:35.863535

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1cfcdbd5dd5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'vaccine_cards', ['cpf'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'vaccine_cards', type_='unique')
    # ### end Alembic commands ###
