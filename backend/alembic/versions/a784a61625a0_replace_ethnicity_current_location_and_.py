"""Replace ethnicity, current location and postal code

Revision ID: a784a61625a0
Revises: 93833e7cdbd5
Create Date: 2020-06-30 03:47:44.540184

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "a784a61625a0"
down_revision = "93833e7cdbd5"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "stories", sa.Column("city", sa.String(length=128), nullable=True)
    )
    op.add_column(
        "stories", sa.Column("country", sa.String(length=128), nullable=True)
    )
    op.add_column(
        "stories", sa.Column("state", sa.String(length=64), nullable=True)
    )
    op.drop_column("stories", "ethnicity")
    op.drop_column("stories", "postal_code")
    op.drop_column("stories", "current_location")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "stories",
        sa.Column(
            "current_location", mysql.VARCHAR(length=128), nullable=True
        ),
    )
    op.add_column(
        "stories",
        sa.Column("postal_code", mysql.VARCHAR(length=64), nullable=True),
    )
    op.add_column(
        "stories",
        sa.Column("ethnicity", mysql.VARCHAR(length=128), nullable=True),
    )
    op.drop_column("stories", "state")
    op.drop_column("stories", "country")
    op.drop_column("stories", "city")
    # ### end Alembic commands ###