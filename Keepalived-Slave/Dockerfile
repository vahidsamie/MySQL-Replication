# Use an Ubuntu base image
FROM ubuntu:latest

# Install necessary packages
RUN apt update && apt install -y keepalived mysql-client netcat  && rm -rf /var/lib/apt/lists/*

# Copy the keepalived configuration file
COPY keepalived.conf /etc/keepalived/keepalived.conf

# Copy the check_mysql script
COPY check_mysql.sh /etc/keepalived/check_mysql.sh
RUN chmod +x /etc/keepalived/check_mysql.sh

# Create a user for script execution
RUN useradd -r keepalived_script

# Start Keepalived
CMD ["keepalived", "-n", "-l"]
