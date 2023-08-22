# Containerized MySQL Failover Cluster With Keepalived
This article provides a simple step-by-step guide to setting up MySQL replication using Dockerfile. Rather than using fancy words to make the article longer, I will provide clear and concise steps to set up MySql replication with Dockerfile.
MySQL replication is a process that allows you to automatically copy data from one database server to another.
In this article, I will show how to configure master-slave replication and also use keepalived service for fault tolerance or automatic failover.
            [![senrio2](https://github.com/vahidsamie/MySQL-Replication/assets/110447267/a9cf3059-804d-4ac2-89a7-5ea8bf1808cb =10x10)] 
# Prerequisites
  1-It is important to have a basic understanding of the concept, f you are unfamiliar with it, you can refer to the documentation provided by [MySQL](https://dev.mysql.com/doc/refman/8.0/en/replication.html)
  
  2- A basic understanding of Docker is necessary for the setup process
# Install docker
Install Docker on your machine and make sure it's running. You may follow the official [Docker documentation](https://docs.docker.com/engine/install/ubuntu/) to install Docker.
# Get docker files ready
I have created a directory named ~docker/mysql and two subdirectories, namely primary and secondary. The primary directory will store the files for the master MySQL server, while secondary will contain the files for the first slave server.

