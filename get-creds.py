#!/usr/bin/env python3

import socket
import webbrowser
from configparser import SafeConfigParser

from settings import *


def read_config(path):
    config = SafeConfigParser()
    config.read(path)
    return config


def write_config(path, config):
    with open(path, "w") as destination:
        config.write(destination)


def device_registration(client_name, client_type):
    try:
        response_client_registration = CLIENT.register_client(
            clientName=client_name,
            clientType=client_type,
        )
        return response_client_registration['clientId'], response_client_registration['clientSecret']
    except Exception as e:
        return e


def get_auth_device(id, secret, start_url):
    try:
        response_device_authorization = CLIENT.start_device_authorization(
            clientId=id,
            clientSecret=secret,
            startUrl=start_url
        )
        return response_device_authorization['verificationUriComplete'], response_device_authorization['deviceCode'], \
               response_device_authorization['userCode']
    except Exception as e:
        return e


def get_token(id, secret, device_code, user_code):
    try:
        response_token_creation = CLIENT.create_token(
            clientId=id,
            clientSecret=secret,
            grantType='urn:ietf:params:oauth:grant-type:device_code',  # review
            deviceCode=device_code,
            code=user_code
        )
        return response_token_creation['accessToken']
    except Exception as e:
        return e


def get_list_accounts(token):
    try:
        response_list_accounts = SSO_CLIENT.list_accounts(
            # nextToken='string',
            maxResults=123,
            accessToken=token
        )
        return response_list_accounts['accountList']
    except Exception as e:
        return e


def get_roles_account(token, accountid):
    try:
        response_account_roles = SSO_CLIENT.list_account_roles(
            # nextToken='string',
            maxResults=123,
            accessToken=token,
            accountId=accountid
        )
        return response_account_roles['roleList']
    except Exception as e:
        return e


def get_roles_credentials(rolename, accountid, token):
    try:
        response_role_credentials = SSO_CLIENT.get_role_credentials(
            roleName=rolename,
            accountId=accountid,
            accessToken=token
        )
        return response_role_credentials['roleCredentials']
    except Exception as e:
        return e


def update_aws_credentials(profile_name, profile, credentials):
    region = AWS_DEFAULT_REGION
    config = read_config(AWS_CREDENTIAL_PATH)
    full_name = profile_name + "-" + profile
    if config.has_section(full_name):
        config.remove_section(full_name)
    config.add_section(full_name)
    config.set(full_name, "region", region)
    config.set(full_name, "aws_access_key_id", credentials["accessKeyId"])
    config.set(full_name, "aws_secret_access_key ", credentials["secretAccessKey"])
    config.set(full_name, "aws_session_token", credentials["sessionToken"])
    write_config(AWS_CREDENTIAL_PATH, config)


def main():
    clientId, clientSecrets = device_registration(socket.gethostname(), 'public')
    url, deviceCode, userCode = get_auth_device(clientId, clientSecrets, SSO_START_URL)
    
    try:
        webbrowser.open(url)
    except:
        print("Please manual login: %s \n" % url)
    
    input("After login, press Enter to continue...")
    
    token = get_token(clientId, clientSecrets, deviceCode, userCode)
    
    accounts_list = get_list_accounts(token)
    
    for account in accounts_list:
        account_id = account['accountId']
        account_name = account['accountName']
        role_name_data = get_roles_account(token, account_id)
        for roleName in role_name_data:
            role_name = roleName['roleName']
            account = roleName['accountId']
            temp_credentials = get_roles_credentials(role_name, account, token)
            print(account_name, 'created')
            update_aws_credentials(account_name, role_name, temp_credentials)


if __name__ == "__main__":
    main()
