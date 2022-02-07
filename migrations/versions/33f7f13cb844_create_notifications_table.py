"""create_notifications_table

Revision ID: 33f7f13cb844
Revises: 29f2b9d64b4e
Create Date: 2021-07-03 16:19:06.653842

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, func, ForeignKey

revision = '33f7f13cb844'
down_revision = '29f2b9d64b4e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('notifications',
                    Column('id', Integer, primary_key=True, index=True),
                    Column('user_id', Integer,ForeignKey("users.id")),
                    Column('is_viewed', Boolean),
                    Column('message', String(500)),
                    Column('url', Text),
                    Column('updated_at', DateTime(
                        timezone=True), onupdate=func.now()),
                    Column('created_at', DateTime(timezone=True),
                           server_default=func.now())
                    )


def downgrade():
    op.drop_table('notifications')
