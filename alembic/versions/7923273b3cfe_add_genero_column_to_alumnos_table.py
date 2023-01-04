"""Add genero column to alumnos table

Revision ID: 7923273b3cfe
Revises: 949c20a28795
Create Date: 2023-01-03 22:25:26.925137

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7923273b3cfe'
down_revision = '949c20a28795'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("alumnos",
            sa.Column("genero", sa.String())
    )


def downgrade() -> None:
    op.drop_column("alumnos", "genero")
