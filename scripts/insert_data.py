import json
import os
from azure.cosmos import CosmosClient
from dotenv import load_dotenv

# Load .env file
load_dotenv()


url = os.getenv('AZURE_URL')
key = os.getenv('AZURE_KEY')
database_name = os.getenv('AZURE_DATABASE')
container_name = os.getenv('AZURE_CONTAINER')


def upload_data_to_cosmosdb(json_file):

    # Initialize the Cosmos client
    client = CosmosClient(url, credential=key)
    database = client.get_database_client(database_name)
    container = database.get_container_client(container_name)

    # Load data from JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Upload data to Cosmos DB container
    for item in data:
        container.upsert_item(item)

    print(f"Data from {json_file} has been uploaded to Cosmos DB!")


# Example usage
upload_data_to_cosmosdb('ModifiedPlusOne.json')
