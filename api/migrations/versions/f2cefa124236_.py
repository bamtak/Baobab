"""empty message

Revision ID: f2cefa124236
Revises: eac3fd9d5ae8
Create Date: 2019-07-04 10:26:14.607764

"""

# revision identifiers, used by Alembic.
revision = 'f2cefa124236'
down_revision = 'eac3fd9d5ae8'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('invitation_letter_request', 'invitation_letter_sent_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('invitation_letter_request', 'invitation_letter_sent_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    # ### end Alembic commands ###
