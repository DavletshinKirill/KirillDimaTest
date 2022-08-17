"""empty message

Revision ID: 96033bbd21ec
Revises: a17380231a74
Create Date: 2022-08-01 12:23:06.809858

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96033bbd21ec'
down_revision = 'a17380231a74'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('users_user_note_fkey', 'users', type_='foreignkey')
    op.drop_column('users', 'user_note')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('user_note', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('users_user_note_fkey', 'users', 'notes', ['user_note'], ['id'])
    # ### end Alembic commands ###
