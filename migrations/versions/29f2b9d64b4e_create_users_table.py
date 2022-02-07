"""Create users table

Revision ID: 29f2b9d64b4e
Revises:
Create Date: 2021-07-02 10:29:52.962055

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, String, Integer, Text, DateTime, Boolean
from sqlalchemy.sql import func

# revision identifiers, used by Alembic.
revision = '29f2b9d64b4e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    Column('id', Integer, primary_key=True, index=True),
                    Column('email', String(255)),
                    Column('password_hash', Text),
                    Column('first_name', String(255)),
                    Column('last_name', String(255)),
                    Column('phone', String(255)),
                    Column('company', String(255)),
                    Column('is_active', Boolean),
                    Column('is_verified', Boolean),
                    Column('locale', String(255)),
                    Column('role', String(255)),
                    Column('photo_url', Text),
                    Column('updated_at', DateTime(
                        timezone=True), onupdate=func.now()),
                    Column('created_at', DateTime(timezone=True),
                           server_default=func.now())
                    )


def downgrade():
    op.drop_table('users')
