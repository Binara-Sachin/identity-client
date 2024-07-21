from common_util import load_public_keys_from_folder, find_signing_key, get_abs_path
from password_grant import get_token
import constants

response = get_token(constants.CLIENT_ID, constants.CLIENT_SECRET, constants.ADMIN_USERNAME, constants.ADMIN_PASSWORD)
jwt_token = response.get('id_token')

folder_path = get_abs_path('../keys/')

public_keys = load_public_keys_from_folder(folder_path)
key_name = find_signing_key(jwt_token, public_keys)

if key_name:
    print(f"The JWT token was signed using the public key in file: {key_name}")
else:
    print("No matching public key found for the JWT token.")

