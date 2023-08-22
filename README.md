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

docker run -d --name mysql-master -p 3306:3306     --env-file .env.primary    -v /root/msql-dockerfile/primary_my.cnf:/etc/mysql/conf.d/my.cnf     -v /root/msql-dockerfile/mysqllib:/var/lib/mysql     -v /root/msql-dockerfile/mysqllog:/var/log/mysql     mysql-image-master

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

 # Please proceed as above.

# Start slave
mysql > START SLAVE;

Use the command below to verify if the secondary server is prepared to receive replication data from the primary server.

mysql > SHOW SLAVE STATUS\G;

You must see the response like give below image.

![mysql](https://github.com/vahidsamie/MySQL-Replication/assets/110447267/a1f2baaf-b907-4daa-be8f-af9a3b553d98)

The Mysql-replication setup is complete, and my final suggestion is to establish a user account on the secondary server with read-only access. By utilizing this account to access data, we can prevent any inadvertent writing to the secondary server.
If you wish to learn about the next steps on how to redirect traffic between the master and slave servers, you can subscribe to my newsletter.


# Log in to the MySQL server on the master container:

    docker exec -it mysql_master_container mysql -umysqluser -p

 ## Use the Database:
Switch to the "userinfo" database:

    USE  UserInfo;

## Verify Data:
You can check the inserted data by running a SELECT query:

    SELECT * FROM users;





# Install and Configure Keepalived on both servers:

Files for keepalive-Master (10.1.1.1):

![keep-master](https://github.com/vahidsamie/MySQL-Replication/assets/110447267/3319a93d-c8ed-426a-b046-53ca7c647bab)

Files for keepalive-Master (10.1.1.2):

![keep-slave](https://github.com/vahidsamie/MySQL-Replication/assets/110447267/32ff17ef-025f-4013-805b-6f9596c1280b)


 1- Create a Dockerfile to build a Keepalived container with the necessary configurations.


 2- Create a Keepalived configuration file named keepalived.conf in the same 
 directory as the Dockerfile.

 3- Create a shell script named chk_mysql.sh that will be used by Keepalived to   check the health of the MySQL service on the master server.

 4- Build and Run Keepalived Container.
    
     docker build -t my-keepalived-image .
     
5- Run the container on both servers:
  
    docker run -d  --name keepalived-container --net=host --cap-add=NET_ADMIN --cap-add=NET_BROADCAST --cap-add=NET_RAW   my-keepalived-image
6-Monitor and Verify:

    docker logs -f keepalived-master
    docker logs -f keepalived-slave


# Install and Configure Flask App on both servers:

## 1- Create the Flask App:

First, create a Python file (app.py).

## 2- Create a Dockerfile for the Flask App:

create a Dockerfile in the same directory as your app.py

## 3- Create a requirements.txt File:

Create a requirements.txt file in the same directory as your app.py

## 4- Build and Run the Docker Container:
    docker build -t flask-api .
    docker run -d -p 5000:5000 --name flask-api-container flask-api
## 5- Step 5: Access the API in the Browser:
   With the Flask API container running, you can access the user information by visiting http://VirtualIP(10.1.1.3):5000 in your web browser. The API will fetch user information from the MySQL database and display it as JSON data in the browser.

   The Flask API instances (user1 and user2 endpoints) should now be accessible. You can access user1 and user2 information by visiting the following URLs in your web browser:

       http://VirtualIP(10.1.1.3):5000/API/1: Show information about user1.
       http://VirtualIP(10.1.1.3):5000/API/2: Show information about user2.
       
![App1](https://github.com/vahidsamie/MySQL-Replication/assets/110447267/569d6baf-f010-4cde-94a7-1e49d70cd0fb)

![api2](https://github.com/vahidsamie/MySQL-Replication/assets/110447267/ea0cb581-f0f2-47c1-af44-aa0ceb5a9a78)


