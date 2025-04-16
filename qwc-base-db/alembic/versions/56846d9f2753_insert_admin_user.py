"""Insert admin user

Revision ID: 56846d9f2753
Revises: f805e8e4a791
Create Date: 2018-07-03 13:13:36.555067

"""
import os
from alembic import op
import sqlalchemy as sa

qwc_config_schema = os.getenv("QWC_CONFIG_SCHEMA", "qwc_config")

# revision identifiers, used by Alembic.
revision = '56846d9f2753'
down_revision = 'f805e8e4a791'
branch_labels = None
depends_on = None


def upgrade():
    # >>> from werkzeug.security import generate_password_hash
    # >>> print(generate_password_hash('admin'))
    sql = sa.sql.text("""
        INSERT INTO {schema}.roles (name, description)
          VALUES ('admin', 'Administrator role');
        INSERT INTO {schema}.users (name, description, password_hash)
          VALUES ('admin', 'Default admin user', 'pbkdf2:sha256:50000$HnkznZ75$43a7c397b974757380b126f6e2cea51b533027b1d0eda3de2d248645c8f9d6cb');
        INSERT INTO {schema}.users_roles (user_id, role_id)
          VALUES ((SELECT id FROM {schema}.users WHERE name = 'admin'), (SELECT id FROM {schema}.roles WHERE name = 'admin'));
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)


def downgrade():
    sql = sa.sql.text("""
        DELETE FROM {schema}.users_roles
          WHERE user_id = (SELECT id FROM {schema}.users WHERE name = 'admin')
            OR role_id = (SELECT id FROM {schema}.roles WHERE name = 'admin');
        DELETE FROM {schema}.users WHERE name = 'admin';
        DELETE FROM {schema}.roles WHERE name = 'admin';
    """.format(schema=qwc_config_schema))

    conn = op.get_bind()
    conn.execute(sql)
