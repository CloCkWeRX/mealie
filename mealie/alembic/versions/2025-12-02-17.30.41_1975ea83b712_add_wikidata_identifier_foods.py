"""Add a wikidata identifier to foods

Revision ID: ARGH
Revises: ARGH
Create Date:
"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "ARGH"
down_revision = "ARGH"
branch_labels: str | tuple[str, ...] | None = None
depends_on: str | tuple[str, ...] | None = None


def upgrade():
    with op.batch_alter_table("ingredient_foods") as batch_op:
        batch_op.add_column(sa.Column("wikidata_identifer", sa.String()))


def downgrade():
    with op.batch_alter_table("ingredient_foods") as batch_op:
        batch_op.drop_column("wikidata_identifer")
