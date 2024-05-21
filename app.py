from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB, VPC
from diagrams.aws.security import KMS

with Diagram("AWS Infrastructure", show=False):

    with Cluster("VPC"):
        vpc = VPC("VPC")

        # with Cluster("Public Subnets"):
        #     public_subnet_group = SubnetGroup("Public Subnet Group")

        # with Cluster("Private Subnets"):
        #     private_subnet_group = SubnetGroup("Private Subnet Group")

    with Cluster("Load Balancers"):
        elb_1 = ELB("ELB 1")
        elb_2 = ELB("ELB 2")

    with Cluster("Database"):
        db_instance_1 = RDS("DB Instance 1")
        db_instance_2 = RDS("DB Instance 2")

    with Cluster("On-Premises"):
        on_premises = VPC("On-Premises")

    vpc >> elb_1
    vpc >> elb_2

    vpc >> db_instance_1
    vpc >> db_instance_2

    vpc << VPCPeering("VPC Peering") << on_premises

    public_subnet_group >> elb_1
    public_subnet_group >> elb_2

    private_subnet_group >> db_instance_1
    private_subnet_group >> db_instance_2

    KMS("KMS Key") >> db_instance_1
    KMS("KMS Key") >> db_instance_2

diagram = Diagram("AWS Infrastructure", show=False)
diagram.save("aws_infrastructure.png")