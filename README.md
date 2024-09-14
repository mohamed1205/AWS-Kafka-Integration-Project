# AWS Kafka Integration Project
In this project, I will execute an End-To-End Data Engineering Project on Real-Time Stock Market Data using Kafka.  We are going to use different technologies such as Python, Amazon Web Services (AWS), Apache Kafka, Glue, Athena, and SQL.

![Architecture](https://github.com/user-attachments/assets/79b7c7b1-4994-48be-8cb0-1a15d51f6a2a)

This guide outlines the steps to set up a data streaming pipeline using Kafka on an AWS EC2 instance and integrate it with various AWS services.

## Prerequisites

AWS Account: Create an account on AWS.

Python 3.11: Install Python 3.11 on your local machine (required for compatibility with kafka-python library).

AWS CLI: Install the AWS CLI on your local machine.

Step-by-Step Guide

## 1. Create an EC2 Instance
- Log in to your AWS account.
- Navigate to the EC2 Dashboard and launch a new EC2 instance.
- Select the Amazon Linux 2 AMI (HVM) for the instance.
- Allow inbound traffic by modifying the security group settings.
- Generate an SSH key pair and download it for accessing the instance.
  
## 2. Access EC2 Instance via SSH
From your local machine, use the SSH key pair to access the EC2 instance:

 **ssh -i /path/to/your-key.pem ec2-user@<EC2-Instance-Public-IP>**

## 3. Install and Set Up Kafka on EC2
Once inside the EC2 instance, install Kafka. Use the following steps (or the commands found in the attached command_kafka.txt file):
- Download Kafka.
- Start Zookeeper.
- Start the Kafka server.
- Create a Kafka topic.
- Start a Kafka producer and consumer.
## 4. Access Your AWS Account Locally via AWS CLI
- On your local machine, create an IAM user in your AWS account.

- Generate an access key for the IAM user to enable programmatic access.

- Configure the AWS CLI with the generated key pair:

 **aws configure**

- Enter the AWS Access Key ID, Secret Access Key, Region, and Output format as prompted.

## 5. Install kafka-python Library
- On your local machine, install the kafka-python library, which will allow you to write Kafka producer and consumer scripts:

 **pip install kafka-python**

- Create producer and consumer scripts (similar to the attached files).

## 6. Set Up AWS Glue Crawlers
- Go to the AWS Glue console.
- Create a new crawler and configure it to use an IAM role that allows it to integrate with other AWS services (e.g., S3, Athena).
- Run the crawler to scan data and create metadata tables in the AWS Glue Data Catalog.
  
## 7. Query Data in AWS Athena
- Navigate to the AWS Athena console.
- Set the AWS Glue Data Catalog as the source.
- Select the created database and run SQL queries on the data.
