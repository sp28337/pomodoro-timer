"""ref-user-profile

Revision ID: eaf888091813
Revises: 606c39073d3c
Create Date: 2024-09-22 16:48:39.940603

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eaf888091813'
down_revision: Union[str, None] = '606c39073d3c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('UserProfile', 'username',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('UserProfile', 'password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('UserProfile', 'password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('UserProfile', 'username',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
