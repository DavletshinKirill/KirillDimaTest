"""empty message

Revision ID: 0c036fc4034c
Revises: f6ff383d8011
Create Date: 2022-08-01 12:16:13.835168

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c036fc4034c'
down_revision = 'f6ff383d8011'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('notes_users')
    op.add_column('users', sa.Column('user_note', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'notes', ['user_note'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'user_note')
    op.create_table('notes_users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('note', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['note'], ['notes.id'], name='notes_users_note_fkey'),
    sa.ForeignKeyConstraint(['user'], ['users.id'], name='notes_users_user_fkey'),
    sa.PrimaryKeyConstraint('id', name='notes_users_pkey')
    )
    # ### end Alembic commands ###
