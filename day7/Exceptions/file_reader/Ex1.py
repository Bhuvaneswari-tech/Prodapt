def read_file(filename):
    try:
        with open(filename,"r") as file:
            content = file.read()
            print("File Content:\n", content)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print("File read successfully!")
    finally:
        print("Operation completed.\n")
        
# Example usage
filename = input("Enter filename to read: ")
read_file(filename)