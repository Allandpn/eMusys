"""alterado tabela unidade

Revision ID: 0262f5d7353c
Revises: 735eaa47189f
Create Date: 2023-12-24 00:03:42.490476

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0262f5d7353c'
down_revision = '735eaa47189f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('unidade', schema=None) as batch_op:
        batch_op.add_column(sa.Column('gestor', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('email', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('telefone', sa.String(length=20), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('unidade', schema=None) as batch_op:
        batch_op.drop_column('telefone')
        batch_op.drop_column('email')
        batch_op.drop_column('gestor')

    # ### end Alembic commands ###
