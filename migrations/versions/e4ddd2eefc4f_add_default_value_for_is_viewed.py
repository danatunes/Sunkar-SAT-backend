"""add default value for is_viewed

Revision ID: e4ddd2eefc4f
Revises: 33f7f13cb844
Create Date: 2021-07-07 17:10:18.610085

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4ddd2eefc4f'
down_revision = '33f7f13cb844'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('notifications','is_viewed',server_default="False")


def downgrade():
    op.alter_column('notifications','is_viewed',server_default=None)