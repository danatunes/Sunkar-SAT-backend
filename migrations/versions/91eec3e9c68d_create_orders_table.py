"""“create_orders_table”

Revision ID: 91eec3e9c68d
Revises: 29f2b9d64b4e
Create Date: 2021-07-03 16:22:35.805017

"""
from alembic import op
from sqlalchemy import ForeignKey, Column, String, Integer, Text, DateTime, Numeric
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision = '91eec3e9c68d'
down_revision = '29f2b9d64b4e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('orders',
                    Column('id', Integer, primary_key=True, index=True),
                    Column('user_id', Integer,ForeignKey("users.id")),
                    Column('price', Numeric(15, 2)),
                    Column('currency', String(255)),
                    Column('coverage', Integer),
                    Column('stage', String(255)),
                    Column('download_url', Text),
                    Column('updated_at', DateTime(
                        timezone=True), onupdate=func.now()),
                    Column('created_at', DateTime(timezone=True),
                           server_default=func.now())
                    )


def downgrade():
    op.drop_table('orders')
