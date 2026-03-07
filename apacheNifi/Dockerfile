# Use official NiFi image
FROM apache/nifi:latest

# Switch to root to install driver
USER root

# Create drivers directory (if not exists)
RUN mkdir -p /opt/nifi/nifi-current/drivers

# Download MySQL JDBC driver
RUN curl -L -o /opt/nifi/nifi-current/drivers/mysql-connector-java-8.0.19.jar \
    https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.19/mysql-connector-java-8.0.19.jar

# Download Parquet and Hadoop NARs into lib folder
RUN curl -L -o /opt/nifi/nifi-current/lib/nifi-parquet-nar-2.8.0.nar \
    https://repo1.maven.org/maven2/org/apache/nifi/nifi-parquet-nar/2.8.0/nifi-parquet-nar-2.8.0.nar

RUN curl -L -o /opt/nifi/nifi-current/lib/nifi-hadoop-libraries-nar-2.8.0.nar \
    https://repo1.maven.org/maven2/org/apache/nifi/nifi-hadoop-libraries-nar/2.8.0/nifi-hadoop-libraries-nar-2.8.0.nar
