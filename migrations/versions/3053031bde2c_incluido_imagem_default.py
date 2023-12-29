"""incluido imagem default

Revision ID: 3053031bde2c
Revises: 5042d718abbf
Create Date: 2023-12-23 18:48:43.686830

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3053031bde2c'
down_revision = '5042d718abbf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('admin', schema=None) as batch_op:
        batch_op.drop_column('image_file')

    with op.batch_alter_table('aluno', schema=None) as batch_op:
        batch_op.drop_column('image_file')

    with op.batch_alter_table('coordenador', schema=None) as batch_op:
        batch_op.drop_column('image_file')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('coordenador', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_file', sa.VARCHAR(length=20), nullable=True))

    with op.batch_alter_table('aluno', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_file', sa.VARCHAR(length=20), nullable=True))

    with op.batch_alter_table('admin', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_file', sa.VARCHAR(length=20), nullable=True))

    # ### end Alembic commands ###
