"""subiendo fecha en tabla de conversation

Revision ID: 58c1208b4c16
Revises: 529290afddff
Create Date: 2023-06-04 19:46:20.208272

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58c1208b4c16'
down_revision = '529290afddff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('conversations', schema=None) as batch_op:
        batch_op.add_column(sa.Column('fecha', sa.String(length=120), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('conversations', schema=None) as batch_op:
        batch_op.drop_column('fecha')

    # ### end Alembic commands ###
