"""Add last_sign_in_at and failed_sign_in_count to users

Revision ID: 916ed45fa0ba
Revises: 60c460c23acb
Create Date: 2018-12-12 10:41:04.687232

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = '916ed45fa0ba'
down_revision = '60c460c23acb'
branch_labels = None
depends_on = None


def upgrade():
    sql = sa.sql.text("""
        ALTER TABLE {schema}.users
          ADD COLUMN last_sign_in_at timestamp without time zone;
        ALTER TABLE {schema}.users
          ADD COLUMN failed_sign_in_count integer DEFAULT 0;
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        ALTER TABLE {schema}.users
          DROP COLUMN last_sign_in_at;
        ALTER TABLE {schema}.users
          DROP COLUMN failed_sign_in_count;
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)
