#!/bin/bash
set -e

# ... (existing script content)

# Add your SQL commands here
if [ "$1" = 'mysqld' ]; then
    mysql -uroot -p"$MYSQL_ROOT_PASSWORD" <<EOF
        GRANT CREATE, CREATE USER ON *.* TO 'vahid'@'%';
        CREATE USER 'replication'@'%' IDENTIFIED BY 'yourpassword';
        GRANT REPLICATION SLAVE ON *.* TO 'replication'@'%';
        CREATE DATABASE UserInfo;
        USE UserInfo;
        CREATE TABLE users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50),
            age INT,
            phone VARCHAR(15),
            location VARCHAR(100),
            gender VARCHAR(10)
        );
    EOF

    exec "$@"
fi
