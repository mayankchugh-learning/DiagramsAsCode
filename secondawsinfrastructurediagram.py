from diagrams import Cluster, Diagram
from diagrams.aws import Edge
from diagrams.aws.compute import EC2AutoScaling
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB, InternetGateway, NATGateway, RouteTable, VPC
from diagrams.aws.security import IAMRole
from diagrams.aws.storage import S3
from diagrams.generic.network import Firewall

with Diagram("AWS Infrastructure with VPN Connection", show=False, outformat="png") as diagram:
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

    # Add animation to the diagram
    edge1 = Edge(firewall, private_route_table, label="VPN Connection", style="dashed", color="red", penwidth="2")
    edge2 = Edge(public_lb, web_instances_public, label="Flow", penwidth="2", headport="n", tailport="s")
    edge3 = Edge(private_lb, web_instances_private, label="Flow", penwidth="2", headport="n", tailport="s")
    edge4 = Edge(web_instances_public, rds_instance, label="Flow", penwidth="2", headport="e", tailport="w")
    edge5 = Edge(web_instances_private, rds_instance, label="Flow", penwidth="2", headport="e", tailport="w")

    diagram += edge1
    diagram += edge2
    diagram += edge3
    diagram += edge4
    diagram += edge5

    # Save each frame of the animation as a PNG image
    diagram.save("aws_infrastructure", format="png", path="frames/", animation=True, animation_fps=2)
