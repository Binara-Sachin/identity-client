from common_util import decode_jwt_token, pretty_print_json, load_public_key, get_abs_path
from password_grant import get_token
import constants

# Replace this with your actual OAuth2 ID token
response = get_token(constants.CLIENT_ID, constants.CLIENT_SECRET, constants.ADMIN_USERNAME, constants.ADMIN_PASSWORD)
token = response.get('id_token')

# Optionally, replace this with your actual public key if needed for verification
public_key = None
public_key = load_public_key(get_abs_path('../keys/wso2carbon.pem'))

decoded_token = decode_jwt_token(token, public_key)
pretty_print_json(decoded_token)
