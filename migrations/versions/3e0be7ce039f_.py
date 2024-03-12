"""empty message

Revision ID: 3e0be7ce039f
Revises: 3dc93569bf1c
Create Date: 2024-03-11 17:15:43.617189

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e0be7ce039f'
down_revision = '3dc93569bf1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(), nullable=True))
        batch_op.create_unique_constraint(None, ['username'])
        batch_op.drop_column('usrname')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('usrname', sa.VARCHAR(), nullable=True))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('username')

    # ### end Alembic commands ###