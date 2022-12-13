"""Interaction with Data Management API."""

import requests
import json
from prettyconf import config

data_manager_base_url = config("DATA_MANAGER_URL")
catalogue_service = config("CATALOG_SERVICE_IDENTIFICATION_UUID")

# Messages
data_manager_get_latest_active_message = data_manager_base_url + f'/manage/service/{catalogue_service}'
data_manager_process_message = data_manager_base_url + f'/manage/service/{catalogue_service}/process/'
data_manager_new_message = data_manager_base_url + f'/manage/message'
data_manager_authentication = data_manager_base_url + f'/manage/authenticate'

# Products
data_manager_get_products_by_category = data_manager_base_url + f''


def get_latest_message_id(username: str) -> str or None:
    """Request Data Management API for latest message id."""
    response = requests.get(url=data_manager_get_latest_active_message + "/" + username)
    message = json.loads(response.content)

    try:
        return message["Active Message List"][0]["content"]["message_uuid"]
    except KeyError:
        pass


def generate_message(target_service, message_content, target_username):
    """Generate message."""

    payload = {
        "service": target_service,
        "username": target_username,
        "detail": message_content
    }

    response = requests.post(url=data_manager_new_message,
                             json=payload)
    message = json.loads(response.content)

    return message


def process_message(message_uuid: str) -> str:
    """Request Data Management API by message uuid."""

    response = requests.put(url=data_manager_process_message + message_uuid)
    message = json.loads(response.content)

    return message["Message Detail"]


def authenticate_user(username: str, password: str):
    """Authenticate User."""
    response = requests.post(url=data_manager_authentication,
                             json={
                                 "username": username,
                                 "password": password
                             })

    message = json.loads(response.content)

    return message
