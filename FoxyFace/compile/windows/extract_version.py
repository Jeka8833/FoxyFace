import json
import argparse

def extract_version(input_file_path, output_file_path):
    """
    Extracts the version from the input JSON file and writes it to the output file.

    Args:
        input_file_path (str): Path to the input JSON file.
        output_file_path (str): Path to the output file.
    """
    try:
        with open(input_file_path, 'r', encoding='utf-8') as infile:
            data = json.load(infile)
            version = data.get("version")

        if version:
            with open(output_file_path, 'w', encoding='utf-8') as outfile:
                outfile.write(version)
            print(f"Version '{version}' successfully written to file '{output_file_path}'")
        else:
            print(f"Error: Key 'version' not found in file '{input_file_path}'")

    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from file '{input_file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extracts the version from a JSON file and writes it to another file.")
    parser.add_argument("input_file", help="Path to the input JSON file (e.g., current_release.json)")
    parser.add_argument("output_file", help="Path to the output file for writing the version")

    args = parser.parse_args()

    extract_version(args.input_file, args.output_file)