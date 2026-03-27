"""Add role column to users

Revision ID: add_role_column_to_users
Revises: 75e97381f656
Create Date: 2026-03-26

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'add_role_column_to_users'
down_revision: Union[str, Sequence[str], None] = '75e97381f656'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.add_column('users', sa.Column('role', sa.String(), nullable=False, server_default='user'))

def downgrade() -> None:
    op.drop_column('users', 'role')
