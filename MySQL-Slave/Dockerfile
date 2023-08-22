# Use the official MySQL image as the base image
FROM mysql:8.0.34

# Install Vim
#RUN apt-get update && apt-get install -y vim
RUN echo "CHANGE MASTER TO MASTER_HOST='185.60.34.14', MASTER_USER='replication', MASTER_PASSWORD='SQ1MasTer1092', MASTER_LOG_FILE='mysql-bin.000004', MASTER_LOG_POS=157;" > /docker-entrypoint-initdb.d/change_master.sql

# Copy the custom my.cnf file to the MySQL container
COPY primary_my.cnf /etc/mysql/conf.d/my.cnf


# Expose the MySQL port
EXPOSE 3306

# Start MySQL with specified options
CMD ["mysqld", \
     "--default-authentication-plugin=mysql_native_password", \
     "--sql_mode=NO_ENGINE_SUBSTITUTION"]
# Create a volume for MySQL data
VOLUME /var/lib/mysql

# Create a volume for MySQL logs
VOLUME /var/log/mysql

#ENTRYPOINT ["/entrypoint.sh"]
ENTRYPOINT ["docker-entrypoint.sh"]
