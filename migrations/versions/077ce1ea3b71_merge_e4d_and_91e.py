"""merge e4d and 91e

Revision ID: 077ce1ea3b71
Revises: e4ddd2eefc4f, 91eec3e9c68d
Create Date: 2021-07-08 17:44:39.409893

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '077ce1ea3b71'
down_revision = ('e4ddd2eefc4f', '91eec3e9c68d')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
