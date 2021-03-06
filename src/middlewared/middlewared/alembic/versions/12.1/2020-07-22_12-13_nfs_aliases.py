"""NFS aliases

Revision ID: 3f06c8533cd3
Revises: 273e1e000675
Create Date: 2020-07-22 12:13:15.609666+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f06c8533cd3'
down_revision = '273e1e000675'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sharing_nfs_share', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nfs_aliases', sa.TEXT(), nullable=True))

    op.execute("UPDATE sharing_nfs_share SET nfs_aliases = '[]'")

    with op.batch_alter_table('sharing_nfs_share', schema=None) as batch_op:
        batch_op.alter_column('nfs_aliases',
               existing_type=sa.TEXT(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sharing_nfs_share', schema=None) as batch_op:
        batch_op.drop_column('nfs_aliases')

    # ### end Alembic commands ###
