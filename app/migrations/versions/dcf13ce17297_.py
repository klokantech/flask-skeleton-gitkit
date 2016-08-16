"""Create schema and insert sample accounts.

Revision ID: dcf13ce17297
Revises: None
Create Date: 2016-05-05 06:18:36.261204

"""

# revision identifiers, used by Alembic.
revision = 'dcf13ce17297'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    account_table = op.create_table(
        'account',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('gitkit_id', sa.Text(), nullable=True),
        sa.Column('email', sa.Text(), nullable=False),
        sa.Column('email_verified', sa.Text(), nullable=False),
        sa.Column('email_challenged', sa.DateTime()),
        sa.Column('name', sa.Text(), nullable=True),
        sa.Column('photo_url', sa.Text(), nullable=True),
        sa.Column('is_admin', sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('account_pkey')),
        sa.UniqueConstraint('email', name=op.f('account_email_key')),
        sa.UniqueConstraint('gitkit_id', name=op.f('account_gitkit_id_key')),
    )
    op.bulk_insert(account_table, [
        {
            'email': 'admin@example.com',
            'email_verified': True,
            'name': 'Administrator',
            'is_admin': True,
        },
        {
            'email': 'john.doe@example.com',
            'email_verified': True,
            'name': 'John Doe',
            'is_admin': False,
        }
    ])


def downgrade():
    op.drop_table('account')
