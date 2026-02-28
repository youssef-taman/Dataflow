# Use official NiFi image
FROM apache/nifi:latest

# Switch to root to install driver
USER root

# Create drivers directory (if not exists)
RUN mkdir -p /opt/nifi/nifi-current/drivers

# Download MySQL JDBC driver
RUN curl -L -o /opt/nifi/nifi-current/drivers/mysql-connector-java-8.0.19.jar \
    https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.19/mysql-connector-java-8.0.19.jar

# Fix permissions so nifi user can read it
RUN chown -R nifi:nifi /opt/nifi/nifi-current/drivers

# Switch back to nifi user
USER nifi