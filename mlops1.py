from diagrams import Cluster, Diagram, Node
from diagrams.aws.compute import Lambda
from diagrams.aws.database import RDS
from diagrams.aws.storage import S3
from diagrams.aws.analytics import Glue
from diagrams.aws.devtools import CodePipeline
from diagrams.onprem.client import User
from diagrams.onprem.ci import Jenkins

with Diagram("MLOps on AWS", show=False):
    with Cluster("Planning"):
        define_problem = User("Define Problem")
        identify_data = User("Identify Data Sources")
        data_collection = Lambda("Data Collection")
        data_preprocessing = Lambda("Data Preprocessing")
        data_splitting = Lambda("Data Splitting")
        feature_engineering = Lambda("Feature Engineering")
        model_selection = Lambda("Model Selection")
        model_training = Lambda("Model Training")
        define_problem >> identify_data >> data_collection >> data_preprocessing >> data_splitting >> feature_engineering >> model_selection >> model_training

    with Cluster("Development"):
        model_evaluation = Lambda("Model Evaluation")
        hyperparameter_tuning = Lambda("Hyperparameter Tuning")
        model_validation = Lambda("Model Validation")
        model_training >> model_evaluation >> hyperparameter_tuning >> model_validation

    with Cluster("Deployment"):
        model_packaging = Lambda("Model Packaging")
        ml_pipeline = CodePipeline("Create ML Pipeline")
        model_deployment = Lambda("Model Deployment")
        model_serving = Lambda("Model Serving")
        api_monitoring = Lambda("API Monitoring")
        model_validation >> model_packaging >> ml_pipeline >> model_deployment >> model_serving >> api_monitoring

    with Cluster("Maintenance"):
        data_feedback = User("Data Feedback")
        model_retraining = Lambda("Model Retraining")
        model_updating = Lambda("Model Updating")
        model_redeployment = Lambda("Model Re-deployment")
        api_monitoring >> data_feedback >> model_retraining >> model_updating >> model_redeployment

    cloudformation = Node("CloudFormation")
    ml_pipeline >> cloudformation
