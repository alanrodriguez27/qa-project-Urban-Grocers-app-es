import configuration
import data
import requests

def create_count(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                        json=body,
                        headers=data.headers)

def create_kit(kit_body,auth_thoken):
    headers = data.headers.copy()
    headers['Authorization'] = f'Bearer {auth_thoken}'
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                        json= kit_body,
                        headers = data.headers
                        )


