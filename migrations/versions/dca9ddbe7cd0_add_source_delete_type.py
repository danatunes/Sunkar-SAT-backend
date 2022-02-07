"""add source delete type

Revision ID: dca9ddbe7cd0
Revises: 4be91e848825
Create Date: 2021-07-16 12:57:40.159672

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
from sqlalchemy import Column, String

revision = 'dca9ddbe7cd0'
down_revision = '4be91e848825'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column("prices", "type")
    op.add_column("prices",
                  Column("source", String())
                  )


def downgrade():
    op.add_column("prices",
                  Column("type", String())
                  )
    op.drop_column("prices", "source")
