import os
import shutil
# from shutil import make_archive

def main():
    file = "text.txt"
    bcfile = file + ".bak"

    if not os.path.exists(file):
        print(f"Error: File '{file}' not found.")
        return
    try:
        shutil.copy(file, bcfile)
        print(f"Successfully Create Backup: '{bcfile}'.")
    except PermissionError:
        print(f"Error: Permission denied to create '{file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == " __main__":
    main()