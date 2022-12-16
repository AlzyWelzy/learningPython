import os

def delete_file(root_dir, file_name):
  # Iterate through all the files and directories in the root directory
  for root, dirs, files in os.walk(root_dir):
    # Check if the file with the specified name is in the current directory
    if file_name in files:
      # If the file is found, delete it
      os.remove(os.path.join(root, file_name))
      print(f"Deleted {file_name} from {root}")

# Test the function
delete_file("./", "tempCodeRunnerFile.py")
