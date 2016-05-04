"""Create schema and sample data.

Revision ID: 0a97d5c5078b
Revises: None
Create Date: 2016-05-04 13:33:41.090862

"""

# revision identifiers, used by Alembic.
revision = '0a97d5c5078b'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    account_table = op.create_table(
        'account',
        sa.Column('id', sa.Text(), nullable=False),
        sa.Column('email', sa.Text(), nullable=False),
        sa.Column('email_verified', sa.Text(), nullable=False),
        sa.Column('name', sa.Text(), nullable=True),
        sa.Column('photo_url', sa.Text(), nullable=True),
        sa.Column('is_admin', sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('account_pkey')),
        sa.UniqueConstraint('email', name=op.f('account_email_key')),
    )
    op.bulk_insert(account_table, [
        {
            'id': '1',
            'email': 'admin@example.com',
            'email_verified': True,
            'name': 'Administrator',
            'is_admin': True,
        },
        {
            'id': '2',
            'email': 'john.doe@example.com',
            'email_verified': True,
            'name': 'John Doe',
            'is_admin': False,
        }
    ])


def downgrade():
    op.drop_table('account')
