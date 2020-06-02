# Get AWS SSO Credentials 

Python Script for updating the local credentials file in your computer using the SSO Login. This script creates a [account-role] entry in your credentials file. 
Each time you run the script it will update each file but not overwrite it. 

## Pre requisites

* Latest Version of the AWS Cli
* Boto 1.13.19 or grater
* Python lib SafeConfigParser
* Python lib pathlib

## Configuration

Before running the script its **important** to update the _settings_ file.

* In _SSO_START_URL_ setting replace the `[YOUR_COMPANY]` value with the corresponding.

* You can to update the default region too.

## Usage

1. Run `python3 get-creds.py`
2. It will take you to the SSO login page. 
3. Enter your credentials.
4. When asked to back to the terminal and press enter. 
5. And that's it! :) 

## References: 

boto3 

    https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-oidc.html
    https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso.html
AWS

    https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_CreateToken.html
    https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/API_RegisterClient.html
    https://docs.aws.amazon.com/singlesignon/latest/PortalAPIReference/API_GetRoleCredentials.html

## Credits

    Facundo Pereyra / f.pereyrap@gmail.com
    Matias Carosso / carossomatias@gmail.com
