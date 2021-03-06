"""add table for storing multiple stories

Revision ID: 2fa6e1a3b8df
Revises: 69b610fddc4b
Create Date: 2020-08-20 23:37:05.405665

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "2fa6e1a3b8df"
down_revision = "69b610fddc4b"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "my_stories",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("text", sa.Text(), nullable=True),
        sa.Column("story_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["story_id"], ["stories.id"],),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_my_stories_id"), "my_stories", ["id"], unique=False
    )

    # data migration: insert old stories into the new my_stories table
    op.execute(
        "INSERT INTO my_stories (story_id, text, updated_at, created_at) "
        + "SELECT stories.id, stories.my_story, NOW(), NOW() "
        + "FROM stories WHERE stories.my_story <> ''"
    )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_my_stories_id"), table_name="my_stories")
    op.drop_table("my_stories")
    # ### end Alembic commands ###
