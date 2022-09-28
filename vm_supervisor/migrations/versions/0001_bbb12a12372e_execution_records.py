"""execution records

Revision ID: bbb12a12372e
Revises: 
Create Date: 2022-09-28 18:52:16.431200

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "bbb12a12372e"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "records",
        sa.Column("uuid", sa.String(), nullable=False),
        sa.Column("vm_hash", sa.String(), nullable=False),
        sa.Column("time_defined", sa.DateTime(), nullable=False),
        sa.Column("time_prepared", sa.DateTime(), nullable=True),
        sa.Column("time_started", sa.DateTime(), nullable=True),
        sa.Column("time_stopping", sa.DateTime(), nullable=True),
        sa.Column("cpu_time_user", sa.Float(), nullable=True),
        sa.Column("cpu_time_system", sa.Float(), nullable=True),
        sa.Column("io_read_count", sa.Integer(), nullable=True),
        sa.Column("io_write_count", sa.Integer(), nullable=True),
        sa.Column("io_read_bytes", sa.Integer(), nullable=True),
        sa.Column("io_write_bytes", sa.Integer(), nullable=True),
        sa.Column("vcpus", sa.Integer(), nullable=False),
        sa.Column("memory", sa.Integer(), nullable=False),
        sa.Column("network_tap", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("uuid"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("records")
    # ### end Alembic commands ###
