# DiagramsAsCode

## How to Use This Repository

## Step 1: Clone this respository

[Langchain GitHub Repository](https://github.com/mayankchugh-learning/LanchainProjects.git)

## Step 2: Create and activate Conda envirnoment

```bash
conda create -p diagremasCodeVEnv python -y
```

## Step 3: Install Dependencies

```bash
source activate ./diagremasCodeVEnv
```
## Step 4: download dependencies

```bash
pip install -r requirements.txt
```

## Step 5: Prompt

```bash
 Generate a diagram (python code) representing an AWS infrastructure setup with a VPC, public and private subnets, load balancers, database instances, and an on-premises connection. You can use the right AWS icons and labels to represent the components. The diagram should include the following elements:

An Internet Gateway connected to the VPC.
A NAT Gateway connected to the private subnets.
A Bastion Host with an Elastic IP.
Public and private subnets within the VPC.
Public and private load balancers.
Web instances in both the public and private subnets.
An RDS instance connected to the web instances.
An S3 bucket connected to the public load balancer.
An on-premises server connected to the infrastructure via a firewall.
```

## Step 5: save the generated code as app.py file and run it in your IDE or terminal.


```bash
Python app.py
```