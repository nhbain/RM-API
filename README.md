# RM-API App

This project deploys a "hello world!" style **FastAPI** app on **AWS Lambda** with **API Gateway** by leveraging **CDK** as its IAC.

## Table of Contents

- [RM-API App](#rm-api-app)
  - [Table of Contents](#table-of-contents)
  - [Package and Infrastructure Overview](#package-and-infrastructure-overview)
  - [Prerequisites](#prerequisites)
  - [Setup Instructions](#setup-instructions)
  - [Running Locally](#running-locally)
    - [With Docker](#with-docker)
    - [Without Docker](#without-docker)
  - [Prior to Deployment](#prior-to-deployment)
    - [CDK Synth](#cdk-synth)
    - [CDK Diff](#cdk-diff)
  - [Deploying the Application](#deploying-the-application)
  - [Testing the API](#testing-the-api)
  - [Cleanup](#cleanup)
  
## Package and Infrastructure Overview

- **FastAPI**: The Python web framework - [FastAPI Docs](https://fastapi.tiangolo.com/)
- **Mangum**: An ASGI adapter that allows FastAPI to run on AWS Lambda - [Mangum Docs](https://mangum.io/)
- **AWS Lambda**: Runs the FastAPI application as a serverless function - [AWS Lambda Docs](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
- **API Gateway**: Exposes the Lambda function as an API endpoint - [API Gateway Docs](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)
- **AWS CDK**: Used to define the infrastructure as code - [Getting Started with AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/work-with-cdk-python.html).

## Prerequisites

Ensure the following tools are installed on your system:

- **Python 3.9** or higher
- **pip** version 22.0 or higher
- **AWS CDK**: To deploy the infrastructure to AWS
- **AWS CLI**: To configure AWS credentials and interact with your AWS account -- make sure you've configured this

## Setup Instructions

1. **Clone the Repository**:
   Clone this repository to your local machine:

   ```bash
   git clone <repository-url>
   cd RM-API
   ```

2. **Set Up a Python Virtual Environment**:
   It’s recommended to create a Python virtual environment to manage dependencies:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Python Dependencies**:
   Install the necessary Python dependencies:

   ```bash
   pip install -r requirements.txt # use requirements-dev.txt if you want to run locally without Docker
   ```

4. **Bootstrap the CDK**:
   If this is your first CDK deployment, you need to bootstrap your AWS environment:

   ```bash
   cdk bootstrap
   ```

## Running Locally

### With Docker

1. **Run Docker Compose**:
   Start the application using the following command:

   ```bash
   docker compose up # add --build if you want to rebuild, or -d to run in detached mode
   ```

   Run the following command to test the endpoint. The url mocks a request as if it's coming through the gateway that feeds Lambda.

    ```bash
    curl -XPOST "http://localhost:8000/2015-03-31/functions/function/invocations" -d '{"resource": "/", "path": "/", "httpMethod": "GET", "requestContext": {}, "multiValueQueryStringParameters": null}'
    ```

    ```bash
    # Windows version
    Invoke-WebRequest -Uri "http://localhost:8000/2015-03-31/functions/function/invocations" -Method POST -Body '{"resource": "/", "path": "/", "httpMethod": "GET", "requestContext": {}, "multiValueQueryStringParameters": null}' -ContentType "application/json"
    ```

### Without Docker

1. **Run the FastAPI Application**:
   Start the application using the following command:

   ```bash
   fastapi dev hello_rm_app.py
   ```

   The application will start on `http://localhost:8000`. Docs are located at `http://localhost:8000/docs`.

## Prior to Deployment

before deploying the stack, you can optionally set some environment variables. They'll be leveraged during stack creation. It primarily simplifies deploying to different environments, but also gives resource naming flexibility.

```text
PROJECT_NAME=rm-api
ENVIRONMENT=dev
REGION_PREFIX=usw2
API_MESSAGE="Hello World!"
```

### CDK Synth

To view the CloudFormation template that will be generated, run the following command:

   ```bash
   cdk synth
   ```

### CDK Diff

To view the changes that will be made to your stack if you've already deployed, run the following command:

   ```bash
   cdk diff
   ```

## Deploying the Application

1. **Deploy the CDK Stack**:
   After setting up the environment, deploy the application to AWS:

   ```bash
   cdk deploy
   ```

   After deployment, the CDK output will provide an API Gateway URL. Use this URL to interact with the API. It can also be interacted with via the AWS Console.

## Testing the API

Once the API is deployed, you can test the endpoint.

1. **CURL, Postman, etc.**
   Use `curl` to test the endpoint:

   ```bash
   curl https://<API_GATEWAY_URL>/
   ```

   Expected response:

   ```json
   {"Greeting": "Hello Raptor Maps!"}
   ```

2. **Browser**
   You can also test it using a browser by navigating to the API Gateway URL

## Cleanup

**DELETE YOUR RESOURCES** if you want to avoid incurring charges. Run the following command to delete the stack:

```bash
cdk destroy
```
