"""
Settings of the project.
"""

import boto3
from pathlib import Path


AWS_DEFAULT_REGION = 'us-east-1'
AWS_CREDENTIAL_PATH = f'{Path.home()}/.aws/credentials'
SSO_START_URL = 'https://cloud[YOUR_COMPANY].awsapps.com/start#/'

CLIENT = boto3.client('sso-oidc', region_name=AWS_DEFAULT_REGION)
SSO_CLIENT = boto3.client('sso', region_name=AWS_DEFAULT_REGION)
