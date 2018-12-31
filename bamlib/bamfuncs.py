import requests
from datetime import datetime
import json


# ACCOUNTS FUNCTIONS
def get_account(account_id=''):

    headers = {
        'content-type': 'application/json',
    }
    base_url = 'https://bank-account-microservice.herokuapp.com/api/accounts/' + str(account_id)

    api_response = requests.request("GET", base_url, headers=headers).json()

    return api_response


def delete_account(account_id=''):

    headers = {
        'content-type': 'application/json',
    }
    base_url = 'https://bank-account-microservice.herokuapp.com/api/accounts/' + str(account_id)

    api_response = requests.request("DELETE", base_url, headers=headers)

    return api_response


def create_account(customer_id, account_type, balance, interest_rate, account_opened=datetime.now()):

    headers = {
        'content-type': 'application/json',
    }
    data = {
        "customer":  customer_id,
        "account_type": account_type,
        "balance": balance,
        "interest_rate": interest_rate,
        "account_opened": str(account_opened)
    }
    data = json.dumps(data)
    base_url = 'https://bank-account-microservice.herokuapp.com/api/accounts/'

    api_response = requests.request("POST", base_url, headers=headers, data=data).json()

    return api_response


def modify_account(account_id='', customer_id=None, account_type=None, balance=None, interest_rate=None, account_opened=None):

    data = json.dumps({key:value for key, value in locals().items() if 'self' not in key and 'account_id' not in key and value})
    headers = {
        'content-type': 'application/json',
    }
    base_url = 'https://bank-account-microservice.herokuapp.com/api/accounts/' + str(account_id) + '/'

    api_response = requests.request("PATCH", base_url, headers=headers, data=data)

    return api_response


# USERS FUNCTIONS
def get_user(user_id=''):

    headers = {
        'content-type': 'application/json',
    }
    base_url = 'https://bank-account-microservice.herokuapp.com/api/users/' + str(user_id)

    api_response = requests.request("GET", base_url, headers=headers).json()

    return api_response


def delete_user(user_id=''):

    headers = {
        'content-type': 'application/json',
    }
    base_url = 'https://bank-account-microservice.herokuapp.com/api/users/' + str(user_id)

    api_response = requests.request("DELETE", base_url, headers=headers)

    return api_response


def create_user(username, email):

    headers = {
        'content-type': 'application/json',
    }
    data = {
        "username":  username,
        "email": email,
        "accounts": []
    }
    data = json.dumps(data)
    base_url = 'https://bank-account-microservice.herokuapp.com/api/users/'

    api_response = requests.request("POST", base_url, headers=headers, data=data).json()
    return api_response


def modify_user(user_id='', username=None, email=None):

    data = json.dumps({key:value for key, value in locals().items() if 'self' not in key and 'user_id' not in key and value})

    headers = {
        'content-type': 'application/json',
    }

    base_url = 'https://bank-account-microservice.herokuapp.com/api/users/' + str(user_id) + '/'

    api_response = requests.request("PATCH", base_url, headers=headers, data=data)

    return api_response
