"""alterado tabela unidade

Revision ID: c79c6ce143b7
Revises: 0262f5d7353c
Create Date: 2023-12-24 03:33:03.868192

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c79c6ce143b7'
down_revision = '0262f5d7353c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('endereco', schema=None) as batch_op:
        batch_op.alter_column('rua',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
        batch_op.alter_column('numero',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('bairro',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('complemento',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('cidade',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('cep',
               existing_type=sa.VARCHAR(length=12),
               nullable=True)
        batch_op.alter_column('estado',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('unidade_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('coordenador_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('aluno_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    with op.batch_alter_table('unidade', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_unidade_nome'), ['nome'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('unidade', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_unidade_nome'), type_='unique')

    with op.batch_alter_table('endereco', schema=None) as batch_op:
        batch_op.alter_column('aluno_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('coordenador_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('unidade_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('estado',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('cep',
               existing_type=sa.VARCHAR(length=12),
               nullable=False)
        batch_op.alter_column('cidade',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('complemento',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('bairro',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('numero',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('rua',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)

    # ### end Alembic commands ###
