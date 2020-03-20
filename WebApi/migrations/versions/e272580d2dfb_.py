"""empty message

Revision ID: e272580d2dfb
Revises: aeacf79231f4
Create Date: 2020-03-20 17:57:43.693556

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mssql

# revision identifiers, used by Alembic.
revision = 'e272580d2dfb'
down_revision = 'aeacf79231f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Channels',
    sa.Column('Id', sa.BigInteger(), nullable=False),
    sa.Column('Name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('Subs',
    sa.Column('User_Id', sa.BigInteger(), nullable=True),
    sa.Column('Channel_Id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['Channel_Id'], ['Channels.Id'], ),
    sa.ForeignKeyConstraint(['User_Id'], ['Players.Id'], )
    )
    op.drop_table('sysdiagrams')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sysdiagrams',
    sa.Column('name', sa.NVARCHAR(length=128), autoincrement=False, nullable=False),
    sa.Column('principal_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('diagram_id', sa.INTEGER(), autoincrement=True, nullable=False, mssql_identity_start=1, mssql_identity_increment=1),
    sa.Column('version', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('definition', mssql.VARBINARY(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('diagram_id', name='PK__sysdiagr__C2B05B6151300EDF')
    )
    op.drop_table('Subs')
    op.drop_table('Channels')
    # ### end Alembic commands ###
