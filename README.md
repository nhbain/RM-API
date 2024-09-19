# RM-API App

This project deploys a "hello world!" style **FastAPI** app on **AWS Lambda** with **API Gateway** by leveraging **CDK** as its IAC.

## Package and Infrastructure Overview

- **FastAPI**: The Python web framework that handles requests - [FastAPI Docs](https://fastapi.tiangolo.com/)
- **Mangum**: An ASGI adapter that allows FastAPI to run on AWS Lambda - [Mangum Docs](https://mangum.io/)
- **AWS Lambda**: Runs the FastAPI application as a serverless function - [AWS Lambda Docs](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
- **API Gateway**: Exposes the Lambda function as an HTTP API endpoint - [API Gateway Docs](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)
- **AWS CDK**: Used to define the infrastructure for the API - [Getting Started with AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/work-with-cdk-python.html).

## Prerequisites

Ensure the following tools are installed on your system:

- **Python 3.9** or higher
- **pip** version 21.0 or higher
- **AWS CDK**: Installed globally using `npm`

  ```bash
  npm install -g aws-cdk
  ```

- **AWS CLI**: To configure AWS credentials and interact with your AWS account.

## Setup Instructions

1. **Clone the Repository**:
   Clone this repository to your local machine:

   ```bash
   git clone <repository-url>
   cd fastapi-serverless-app
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
   pip install -r requirements.txt
   ```

4. **Bootstrap the CDK**:
   If this is your first CDK deployment, you need to bootstrap your AWS environment:

   ```bash
   cdk bootstrap
   ```
