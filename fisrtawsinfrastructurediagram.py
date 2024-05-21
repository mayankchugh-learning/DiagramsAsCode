# Updated Prompt:
# Please generate a diagram representing an AWS infrastructure setup with a VPC, public and private subnets, load balancers,
# database instances, and an on-premises connection. Use appropriate AWS icons and labels to represent the components. The diagram
# should include the following elements:
# - An Internet Gateway connected to the VPC.
# - A NAT Gateway connected to the private subnets.
# - A Bastion Host with an Elastic IP.
# - Public and private subnets within the VPC.
# - Public and private load balancers.
# - Web instances in both the public and private subnets.
# - An RDS instance connected to the web instances.
# - An S3 bucket connected to the public load balancer.
# - An on-premises server connected to the infrastructure via a firewall.

from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2AutoScaling
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB, InternetGateway, NATGateway, RouteTable, VPC
from diagrams.aws.security import IAMRole
from diagrams.aws.storage import S3
from diagrams.generic.network import Firewall

with Diagram("AWS Infrastructure with VPN Connection", show=False):
    internet_gateway = InternetGateway("Internet Gateway")
    nat_gateway = NATGateway("NAT Gateway")
    bastion_host = EC2AutoScaling("Bastion Host")
    elastic_ip = EC2AutoScaling("Elastic IP")

    with Cluster("VPC"):
        with Cluster("Public Subnets"):
            public_route_table = RouteTable("Public Route Table")
            public_lb = ELB("Public Load Balancer")
            web_instances_public = [EC2AutoScaling("Web 1 (Public)"), EC2AutoScaling("Web 2 (Public)")]

        with Cluster("Private Subnets"):
            private_route_table = RouteTable("Private Route Table")
            private_lb = ELB("Private Load Balancer")
            web_instances_private = [EC2AutoScaling("Web 1 (Private)"), EC2AutoScaling("Web 2 (Private)")]
            rds_instance = RDS("RDS Instance")

        public_route_table >> internet_gateway
        private_route_table >> nat_gateway
        bastion_host >> elastic_ip
        elastic_ip >> internet_gateway
        elastic_ip >> bastion_host
        internet_gateway >> public_route_table
        nat_gateway >> private_route_table

        public_lb >> web_instances_public
        private_lb >> web_instances_private
        web_instances_public >> rds_instance
        web_instances_private >> rds_instance

        with Cluster("Database Subnets"):
            db_instance = RDS("Database")

        web_instances_public >> db_instance

    with Cluster("S3 Bucket"):
        s3_bucket = S3("Data Storage")

    public_lb >> s3_bucket

    # IAM Roles
    iam_role_web = IAMRole("IAM Role (Web Instances)")
    iam_role_db = IAMRole("IAM Role (Database)")

    web_instances_public >> iam_role_web
    web_instances_private >> iam_role_web
    db_instance >> iam_role_db

    with Cluster("On-Premises Connection"):
        firewall = Firewall("Firewall")

    firewall >> private_route_table
