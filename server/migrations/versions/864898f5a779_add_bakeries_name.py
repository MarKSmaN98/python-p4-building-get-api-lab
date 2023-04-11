"""add bakeries name

Revision ID: 864898f5a779
Revises: 3f56860cbb31
Create Date: 2023-04-11 10:25:55.486254

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '864898f5a779'
down_revision = '3f56860cbb31'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('bakeries', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('bakeries', schema=None) as batch_op:
        batch_op.drop_column('name')

    # ### end Alembic commands ###
