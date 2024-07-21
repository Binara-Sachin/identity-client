from common_util import decode_oauth2_id_token, pretty_print_json
from password_grant import get_token

# Define the URL and credentials
url = 'https://localhost:9443/oauth2/token'
client_id = 'EiAT_IifIY6_EDopEH_uvTNZytAa'
client_secret = 'TInb1WEoq2sDIB5D1KrQ11fgvNgIc07IRrPTcTdSfJca'
username = 'admin'
password = 'admin'

# Replace this with your actual OAuth2 ID token
response = get_token(client_id, client_secret, username, password)
token = response.get('id_token')

# Optionally, replace this with your actual public key if needed for verification
public_key = None

decoded_token = decode_oauth2_id_token(token, public_key)
pretty_print_json(decoded_token)
