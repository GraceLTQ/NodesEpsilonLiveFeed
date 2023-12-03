import json
import random


def transform_modified_to_try(modified_data):
    transformed_data = []

    for entry in modified_data:
        # Generate random id
        new_id = str(random.randint(1, 100000000))

        # Create the transformed entry with "id" and "sender" at the beginning
        new_entry = {
            "id": new_id,
            "sender": entry["sender"]
        }

        # Add the remaining fields to the new_entry
        for key, value in entry.items():
            if key != "sender":
                new_entry[key] = value

        transformed_data.append(new_entry)

    return transformed_data


# Load your source data
with open('../data/OutputInvestorEmailfromSentItems.json', 'r') as file:
    modified_data = json.load(file)

# Perform the transformation
transformed_data = transform_modified_to_try(modified_data)

# Save the transformed data to a new JSON file
with open('../data/CleanedData.json', 'w') as file:
    json.dump(transformed_data, file, indent=4)
