import os
import shutil
from shutil import make_archive

def main():
    filename = "textfile.txt"
    backup_filename = filename + ".bak"

    if not os.path.exists(filename):
            print(f"Error: File '{filename}' not found.")
            return
    try:
        shutil.copy2(filename, backup_filename)
        print(f"Successfully Create backup: '{backup_filename}'.")
    except PermissionError:
        print(f"Error: Permission denied to create '{backup_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

        





if __name__ == "__main__":
    main()
