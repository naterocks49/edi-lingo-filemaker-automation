"""
Filemaker API helper functions
"""
import base64

def encode_credentials(username, password):
    '''Function to encode username and password to base64 for auth header - returns encoded string'''
    credentials = f"{username}:{password}"
    encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")
    return encoded_credentials