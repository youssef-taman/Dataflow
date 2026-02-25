FROM mysql:8.0

ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=tpch

# Enable server-side    infile
RUN printf "[mysqld]\nlocal_infile=1\n" > /etc/mysql/conf.d/local.cnf


WORKDIR /data
# Copy data files 

COPY ./data/*.tbl /data/

# Copy schema + loader
COPY dss.sql /docker-entrypoint-initdb.d/
COPY load.sh /docker-entrypoint-initdb.d/

RUN chmod +x /docker-entrypoint-initdb.d/load.sh