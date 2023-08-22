# Use the official MySQL image as the base image
FROM mysql:8.0.34
# Copy the primary_my.cnf file to the MySQL configuration directory
COPY primary_my.cnf /etc/mysql/conf.d/my.cnf
# Copy your custom docker-entrypoint.sh script to the container
COPY docker-entrypoint.sh /usr/local/bin/

# Set execute permissions for the script
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

# Expose the MySQL port
EXPOSE 3306
# Set command-line options for MySQL
CMD ["mysqld", \
     "--default-authentication-# Set command-line options for MySQLplugin=mysql_native_password", \
     "--sql_mode=NO_ENGINE_SUBSTITUTION"]

# Create a volume for MySQL data
VOLUME /var/lib/mysql

# Create a volume for MySQL logs
VOLUME /var/log/mysql

# Start the MySQL service
ENTRYPOINT ["docker-entrypoint.sh"]
