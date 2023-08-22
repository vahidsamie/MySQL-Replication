# Containerized MySQL Failover Cluster With Keepalived
This article provides a simple step-by-step guide to setting up MySQL replication using Dockerfile. Rather than using fancy words to make the article longer, I will provide clear and concise steps to set up MySql replication with Dockerfile.
MySQL replication is a process that allows you to automatically copy data from one database server to another.
In this article, I will show how to configure master-slave replication and also use keepalived service for fault tolerance or automatic failover.
![senrio2](https://github.com/vahidsamie/MySQL-Replication/assets/110447267/a9cf3059-804d-4ac2-89a7-5ea8bf1808cb)
            
# Prerequisites
  1-It is important to have a basic understanding of the concept, f you are unfamiliar with it, you can refer to the documentation provided by [MySQL](https://dev.mysql.com/doc/refman/8.0/en/replication.html)
  
  2- A basic understanding of Docker is necessary for the setup process
# Install docker
Install Docker on your machine and make sure it's running. You may follow the official [Docker documentation](https://docs.docker.com/engine/install/ubuntu/) to install Docker.
# Get docker files ready
I have created a directory named ~docker/mysql and two subdirectories, namely primary and secondary. The primary directory will store the files for the master MySQL server, while secondary will contain the files for the first slave server.

# Setup primary/master server
Files for `primary`:

![master](https://github.com/vahidsamie/MySQL-Replication/assets/110447267/6c3eead1-81be-47f4-897c-69b73c185c57)



## .env.primary
write the variables especially credentials to connect with primary(master) Mysql
##  primary_my.cnf
Mysql settings for primary Mysql container

## Dockerfile
Dockerfile to create primary MySQL container.
## docker-entrypoint.sh
Create a new docker-entrypoint.sh script that includes your SQL commands



# Run Dockerfile for primary server
Navigate to the directory where you have stored your primary Dockerfile. In my case, it is located in the directory ~/docker/mysql/primary on Ubuntu.

cd ~/docker/mysql/primary

sudo  docker build -t mysql-master-image- .

## Check if container is created
sudo docker ps


A list of containers will be displayed. Please ensure that the "port" column indicates the port number. If the "port" column is blank, use the following command to check the Docker logs:

sudo docker logs mysql-primary
## Confirm replication
Before proceeding, let us confirm that the primary server is prepared to act as the master and replicate data to the secondary server. Connect to MySQL and verify the replication status, using the server's IP address if it is not hosted locally.

mysql -h 127.0.0.1 -uroot -p

Once you have successfully logged in to MySQL, use the command below to verify the replication status:

mysql> SHOW MASTER STATUS\G;

It will return a response something like below:

*************************** 1. row **************************

             File: mysql-bin.000003
         Position: 157
      Binlog_Do_DB: mydatabase
      Binlog_Ignore_DB: 
    mysqlExecuted_Gtid_Set:*

If the response resembles the snippet above, you are prepared to proceed with setting up the secondary server.
Take note of the mysql-bin.000003 file and 157 position values from the response above. We will utilize these values in the configuration of the secondary server.

# Secondary server setup

 Files for `secondary`:
 
 ![slave](https://github.com/vahidsamie/MySQL-Replication/assets/110447267/4727cd20-6aef-4785-b681-25ff1d75a1bc)

 Please proceed as above.

# Start slave
mysql > START SLAVE;

Use the command below to verify if the secondary server is prepared to receive replication data from the primary server.

mysql > SHOW SLAVE STATUS\G;

You must see the response like give below image.

![1681386298939](https://github.com/vahidsamie/MySQL-Replication/assets/110447267/6fa8c386-8346-447f-81cd-04fc0ec16fac)



 

