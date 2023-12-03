import base64
import binascii
import json
import os
from azure.cosmos import CosmosClient
from dotenv import load_dotenv

# Load .env file
load_dotenv()


key = os.getenv('key')

try:
    decoded_key = base64.b64decode(key)
    print("Key is valid Base64")
except binascii.Error:
    print("Key is not valid Base64")
