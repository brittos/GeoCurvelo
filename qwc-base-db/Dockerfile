# A postgres DB with the minimal QWC config DB setup

ARG PG_MAJOR=17
FROM postgis/postgis:17-3.5

ENV POSTGIS_MAJOR 3
ENV POSTGIS_VERSION 3.5.2+dfsg-1.pgdg110+1
ENV PGDATA=/var/lib/postgresql/data
ENV POSTGRES_PASSWORD=

# ENV for qwc-services database roles passwords
ENV QGIS_SERVER_PASSWORD=qgis_server
ENV QWC_ADMIN_PASSWORD=qwc_admin
ENV QWC_SERVICE_PASSWORD=qwc_service
ENV QWC_SERVICE_WRITE_PASSWORD=qwc_service_write

# Setup database
# script to create DB, roles, grants etc
COPY setup-roles-and-db.sh /docker-entrypoint-initdb.d/0_setup-db.sh
RUN chmod +x /docker-entrypoint-initdb.d/0_setup-db.sh
