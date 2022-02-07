"""migration for price

Revision ID: 51489a893e46
Revises: 077ce1ea3b71
Create Date: 2021-07-09 16:21:00.390334

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
from sqlalchemy import String, Text, Column, Integer, Numeric, DateTime, func

revision = '51489a893e46'
down_revision = '077ce1ea3b71'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('prices',
                    Column('id', Integer, primary_key=True, index=True),
                    Column('satellite', String),
                    Column('acquisition_mode', Text),
                    Column('type', String, nullable=False),
                    Column('processing_level', String, nullable=False),
                    Column('currency', String),
                    Column('price', Numeric(15, 2)),
                    Column('updated_at', DateTime(
                        timezone=True), onupdate=func.now()),
                    Column('created_at', DateTime(timezone=True),
                           server_default=func.now())
                    )


def downgrade():
    op.drop_table('prices')
