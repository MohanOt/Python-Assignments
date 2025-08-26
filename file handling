# File Read & Write Challenge + Error Handling Lab

def read_and_modify_file(input_file, output_file):
    try:
        # Open the input file in read mode
        with open(input_file, 'r') as f:
            content = f.read()

        # Modify content (example: make everything uppercase)
        modified_content = content.upper()

        # Write modified content into new file
        with open(output_file, 'w') as f:
            f.write(modified_content)

        print(f"✅ File '{input_file}' read successfully and written to '{output_file}'.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_file}' does not exist.")
    except PermissionError:
        print(f"❌ Error: You don’t have permission to read '{input_file}'.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# Ask the user for a filename
filename = input("Enter the filename to read: ")

# Create output filename automatically
output_filename = "modified_" + filename

# Call the function
read_and_modify_file(filename, output_filename)
