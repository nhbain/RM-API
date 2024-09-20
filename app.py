import aws_cdk as cdk
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_ecr_assets as ecr_assets,
    aws_apigateway as apigateway
)
from constructs import Construct
import os

def generateResourceName(resource):
    project_name = os.getenv('PROJECT_NAME', "rm-api")
    environment = os.getenv('ENVIRONMENT', "dev")
    region_prefix = os.getenv('REGION_PREFIX', "usw2")
    return f"{project_name}-{environment}-{region_prefix}-{resource}"

class RMAPIStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        api_lambda = _lambda.DockerImageFunction(
            self, generateResourceName("api-lambda"),
            code=_lambda.DockerImageCode.from_image_asset(directory='.'),
            timeout=cdk.Duration.seconds(30)
        )

        api_gateway = apigateway.LambdaRestApi(
            self, generateResourceName("api-gateway"),
            handler=api_lambda,
            proxy=True,
            rest_api_name=f"{os.getenv('PROJECT_NAME', 'RM API')} service"
        )

app = cdk.App()
RMAPIStack(app, generateResourceName("stack"))
app.synth()
