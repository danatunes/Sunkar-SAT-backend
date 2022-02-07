"""create new table order_units

Revision ID: 1d878d5f81ac
Revises: dca9ddbe7cd0
Create Date: 2021-07-16 14:50:19.948418

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from geoalchemy2 import Geometry
from sqlalchemy import Column, Integer, ForeignKey, Text, String, Boolean, JSON, Numeric, DateTime, func

revision = '1d878d5f81ac'
down_revision = 'dca9ddbe7cd0'
branch_labels = None
depends_on = None



def upgrade():
    op.create_table('order_units',
                    Column('id', Integer, primary_key=True, index=True),
                    Column('order_id', Integer, ForeignKey("orders.id")),
                    Column('price_id', Integer, ForeignKey("prices.id")),
                    Column('acquisition_mode', Text, nullable=False),
                    Column('address', String),
                    Column('priority', String),
                    Column('is_express', Boolean),
                    Column('cloud_coverage_start', Integer),
                    Column('cloud_coverage_end', Integer),
                    Column('geom', Geometry),
                    Column('geom_raw', JSON),
                    Column('price', Numeric(15, 2)),
                    Column('currency', Numeric(15, 2)),
                    Column('periods', JSON),
                    Column('satellite', String),
                    Column('wish', String(1000)),
                    Column('application_theme', String),
                    Column('coverage', Integer),
                    Column('is_archive', Boolean),
                    Column('status', String, nullable=False),
                    Column('nadir', Boolean),
                    Column('updated_at', DateTime(
                        timezone=True), onupdate=func.now()),
                    Column('created_at', DateTime(timezone=True),
                           server_default=func.now())
                    )


def downgrade():
    op.drop_table('order_units')
