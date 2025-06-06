from __future__ import with_statement
from alembic import context
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig
import os

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Set variables for config
section = config.config_ini_section
config.set_section_option(section, "PGSERVICE", os.environ.get("PGSERVICE", "qwc_configdb"))
config.set_section_option(section, "QWC_CONFIG_SCHEMA", os.environ.get("QWC_CONFIG_SCHEMA", "qwc_config"))

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = None

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    version_table_schema = config.get_main_option("version_table_schema")
    context.configure(
        url=url, version_table_schema=version_table_schema,
        target_metadata=target_metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool)

    with connectable.connect() as connection:
        version_table_schema = config.get_main_option("version_table_schema")
        context.configure(
            connection=connection,
            version_table_schema=version_table_schema,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
