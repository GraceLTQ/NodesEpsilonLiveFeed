from azure.cosmos import CosmosClient
import json
import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey
import datetime
import config


HOST = config.settings['host']
MASTER_KEY = config.settings['master_key']
DATABASE_ID = config.settings['database_id']
CONTAINER_ID = config.settings['container_id']


def upload_data_to_cosmosdb(json_file):

    # Define your Azure Cosmos DB configuration
    url = 'https://epsilonemaildatabase.documents.azure.com:443/'
    key = 'VNkD0GSMS0hwUPGEenMI0oK99P1kUzpUaZXyNxY9TyYkOOrwb8En4amZFs6mXec4FqZ16iEiwaXvACDbHuXGxA=='
    database_name = 'EpsilonEmailDatabase'
    container_name = 'EpsilonEmailContainer'

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
