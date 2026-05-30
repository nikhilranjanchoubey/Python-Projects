import os

def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f"File '{filename}' created successfully!")

    except FileExistsError:
        print(f"File '{filename}' already exists!")

    except Exception as e:
        print(f"An error occurred: {e}")


def view_all_files():
    files = [file for file in os.listdir() if os.path.isfile(file)]

    if not files:
        print("No files found!")

    else:
        print("\nFiles in Current Directory:")
        for file in files:
            print(file)


def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()

        print(f"\nContent of '{filename}':\n")
        print(content)

    except FileNotFoundError:
        print(f"File '{filename}' does not exist!")

    except Exception as e:
        print(f"An error occurred: {e}")


def edit_file(filename):
    try:
        with open(filename, 'a') as f:
            content = input("Enter data to add: ")
            f.write(content + "\n")

        print(f"Content added to '{filename}' successfully!")

    except FileNotFoundError:
        print(f"File '{filename}' does not exist!")

    except Exception as e:
        print(f"An error occurred: {e}")


def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File '{filename}' deleted successfully!")

    except FileNotFoundError:
        print(f"File '{filename}' not found!")

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    while True:
        print("\n========== FILE MANAGEMENT APP ==========")
        print("1. Create File")
        print("2. View All Files")
        print("3. Read File")
        print("4. Edit File")
        print("5. Delete File")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            filename = input("Enter file name: ")
            create_file(filename)

        elif choice == '2':
            view_all_files()

        elif choice == '3':
            filename = input("Enter file name: ")
            read_file(filename)

        elif choice == '4':
            filename = input("Enter file name: ")
            edit_file(filename)

        elif choice == '5':
            filename = input("Enter file name: ")

            confirm = input(
                f"Are you sure you want to delete '{filename}'? (y/n): "
            )

            if confirm.lower() == 'y':
                delete_file(filename)
            else:
                print("Delete operation cancelled.")

        elif choice == '6':
            print("Thank you for using File Management App!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()