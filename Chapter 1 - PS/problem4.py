# import os

# def print_directory_contents(directory):
#     try:
#         # List all files and directories in the specified directory
#         contents = os.listdir(directory)
        
#         # Print the contents
#         for item in contents:
#             print(item)
#     except FileNotFoundError:
#         print(f"The directory '{directory}' does not exist.")
#     except PermissionError:
#         print(f"Permission denied to access the directory '{directory}'.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Specify the directory path
# directory_path = "/"

# # Print the contents of the specified directory
# print_directory_contents(directory_path)

# ............. OR .............

import os

# Specify the directory path
# directory_path = "/"    # Files & folder in C drive
directory_path = "/Adnan Shaikh"

# List all files and directories in the specified path
contents = os.listdir(directory_path)

# Print the each file and directory name
for item in contents:
    print(item)
