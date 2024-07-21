# password_grant/__init__.py

import requests
import base64
import constants

def get_token(client_id, client_secret, username, password):
    """
    Retrieve an ID token from the identity server.

    :param client_id: Client ID for the identity server.
    :param client_secret: Client secret for the identity server.
    :param username: Username for authentication.
    :param password: Password for authentication.
    :return: ID token and access token if successful, else None.
    """
    url = constants.TOKEN_ENDPOINT_URL

    # Encode client ID and client secret for the Authorization header
    auth_str = f"{client_id}:{client_secret}"
    auth_bytes = auth_str.encode('utf-8')
    auth_base64 = base64.b64encode(auth_bytes).decode('utf-8')

    # Define headers and form data
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Authorization': f'Basic {auth_base64}'
    }

    data = {
        'grant_type': 'password',
        'username': username,
        'password': password,
        'scope': 'openid'
    }

    # Send the POST request
    try:
        response = requests.post(url, headers=headers, data=data, verify=False)  # verify=False for self-signed SSL

        # Check if the request was successful
        if response.status_code == 200:
            response_json = response.json()
            # id_token = response_json.get('id_token')
            # access_token = response_json.get('access_token')
            return response_json
        else:
            print("Failed to retrieve token")
            print("Status Code:", response.status_code)
            print("Response:", response.text)
            return None
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None
