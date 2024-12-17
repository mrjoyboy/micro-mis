import json

def convert_format(input_file, output_file):
    """
    Converts JSON data from the input format to the desired output format.

    Args:
        input_file (str): Path to the input JSON file.
        output_file (str): Path to the output JSON file.
    """
    try:
        # Load data from input file
        with open(input_file, 'r') as infile:
            data = json.load(infile)

        # Transform data to the new format
        transformed_data = []
        for item in data:
            transformed_item = {
                "model": "events.district",
                "pk": item["id"],
                "fields": {
                    "name": item["name"],
                    "province": item["province_id"],
                    "area_sq_km": item["area_sq_km"],
                    "website": item["website"],
                    "headquarter": item["headquarter"]
                }
            }
            transformed_data.append(transformed_item)

        # Write transformed data to output file
        with open(output_file, 'w') as outfile:
            json.dump(transformed_data, outfile, indent=4)

        print(f"Data successfully converted and saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
# Replace 'input.json' and 'output.json' with the actual file paths
convert_format('/home/atreya/Projects/micro-mis/backend/scripts/districts_input.json', '/home/atreya/Projects/micro-mis/backend/scripts/districts_output.json')
