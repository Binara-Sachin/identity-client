import jwt
import json
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.backends import default_backend
import os

def decode_jwt_token(jwt_token, public_key=None):
    """
    Decode an OAuth2 ID token and display its contents.

    :param id_token: The encoded JWT token.
    :param public_key: The public key for verifying the token (if needed).
    :return: Decoded token contents.
    """
    try:
        # header_data = jwt.get_unverified_header(jwt_token)
        # alg = header_data['alg']

        if public_key:
            # decoded = jwt.decode(jwt_token, public_key, algorithms=['RS256'])
            decoded = jwt.decode(jwt_token, public_key, algorithms=['RS256'], options={'verify_aud': False})
        else:
            decoded = jwt.decode(jwt_token, options={"verify_signature": False}, algorithms=['RS256'])

        return decoded

    except jwt.ExpiredSignatureError:
        return {"error": "Token expired"}
    except jwt.InvalidTokenError as e:
        return {"error": f"Invalid token: {e}"}
    except Exception as e:
        return {"error": f"Unexpected error: {e}"}

def pretty_print_json(data):
    """
    Pretty print JSON data.

    :param data: The JSON data to be printed.
    """
    print(json.dumps(data, indent=4, sort_keys=True))

def get_abs_path(relative_path):
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    return os.path.join(script_dir, relative_path)

def load_public_key(file_path):
    with open(file_path, 'rb') as cert_file:
        cert_data = cert_file.read()

    cert = load_pem_x509_certificate(cert_data, default_backend())
    public_key = cert.public_key()
    
    return public_key


# Function to load public keys from .pem files in a folder
def load_public_keys_from_folder(folder_path):
    public_keys = {}
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.pem'):
            file_path = os.path.join(folder_path, file_name)
            try:
                public_key = load_public_key(file_path)
                public_keys[file_name] = public_key
            except ValueError as e:
                print(f"Skipping file {file_name}: {e}")
                
    return public_keys

# Function to decode JWT and find which public key was used to sign it
def find_signing_key(jwt_token, public_keys):
    for key_name, public_key in public_keys.items():
        try:
            # Try to decode the JWT using the current public key
            jwt.decode(jwt_token, public_key, algorithms=['RS256'], options={'verify_aud': False})
            return key_name
        except jwt.ExpiredSignatureError:
            print(f"JWT token expired, but key {key_name} is valid")
        except jwt.InvalidTokenError:
            # If decoding fails, continue with the next key
            continue
    return None