from diagrams import Cluster, Diagram
from diagrams.generic.compute import Rack
from diagrams.generic.network import Switch

with Diagram("Python Application Deployment on AWS", show=False):
    with Cluster("Source"):
        codecommit = Rack("Code\nRepository")

    with Cluster("Build"):
        codebuild = Rack("Code\nBuild")

    with Cluster("Deploy"):
        with Cluster("CodePipeline"):
            codepipeline = Rack("Code\nPipeline")
            s3 = Rack("S3\nBucket")

    with Cluster("Compute"):
        ec2 = Rack("EC2\nInstances")

    with Cluster("Managed Service"):
        elasticbeanstalk = Rack("Elastic\nBeanstalk")

    with Cluster("Deployment Service"):
        codedeploy = Rack("Code\nDeploy")

    codecommit >> codepipeline >> codebuild >> s3 >> codedeploy >> elasticbeanstalk
    elasticbeanstalk >> ec2
