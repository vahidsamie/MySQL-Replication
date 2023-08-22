# Use an Ubuntu base image
FROM ubuntu:22.04

# Install necessary packages
RUN apt update && apt install -y keepalived mysql-client netcat && rm -rf /var/lib/apt/lists/*

# Copy the keepalived configuration file
COPY keepalived.conf /etc/keepalived/keepalived.conf

# Copy the check_mysql script
COPY chk_mysql /etc/keepalived/chk_mysql
RUN chmod +x /etc/keepalived/chk_mysql

# Create a user for script execution
RUN useradd -r keepalived_script

# Start Keepalived
CMD ["keepalived", "-n" , "-D" , "-l" ]
