import jwt
import json

def decode_oauth2_id_token(id_token, public_key=None):
    """
    Decode an OAuth2 ID token and display its contents.

    :param id_token: The encoded JWT token.
    :param public_key: The public key for verifying the token (if needed).
    :return: Decoded token contents.
    """
    try:
        # Decode the token without verification (use this only if you don't need to verify)
        decoded = jwt.decode(id_token, options={"verify_signature": False}, algorithms=["RS256"])

        # If you need to verify the token, use the public key
        # decoded = jwt.decode(id_token, public_key, algorithms=["RS256"])

        return decoded

    except jwt.ExpiredSignatureError:
        return {"error": "Token has expired"}
    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}

def pretty_print_json(data):
    """
    Pretty print JSON data.

    :param data: The JSON data to be printed.
    """
    print(json.dumps(data, indent=4, sort_keys=True))
