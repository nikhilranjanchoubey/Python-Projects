'''
Conditional - to implement a logic
Loops - menu system
Dictionary - store data
'''

# Create an empty dictionary to store student names and marks
student = {}

# Infinite loop to keep the menu running until user exits
while True:

    # Display menu options
    print("\n----STUDENT MANAGER APP----")
    print("1. Add Student")
    print("2. View Student")
    print("3. Check Student")
    print("4. Exit")

    # Take user's choice as input
    choice = input("Enter your choice: ")

    # ---------------- ADD STUDENT ----------------
    if choice == "1":

        # Take student name from user
        name = input("Enter student name: ")

        # Take marks and convert input string to integer
        marks = int(input("Enter marks: "))

        # Store name as key and marks as value in dictionary
        student[name] = marks

        # Success message
        print(f"{name} Successfully Added!")

    # ---------------- VIEW STUDENTS ----------------
    elif choice == "2":

        # Check if dictionary is empty
        if not student:
            print("No Student Found!")

        else:
            # Loop through all dictionary items
            for name, marks in student.items():

                # Display each student's name and marks
                print(name, ":", marks)

    # ---------------- CHECK RESULT ----------------
    elif choice == "3":

        # Ask user which student's result to check
        name = input("Enter Student Name: ")

        # Check whether student exists in dictionary
        if name in student:

            # Retrieve marks of that student
            marks = student[name]

            # Pass/Fail condition
            if marks >= 40:
                print("PASS")
            else:
                print("FAIL")

        # Student not found
        else:
            print("Student Not Found")

    # ---------------- EXIT PROGRAM ----------------
    elif choice == "4":

        # Exit message
        print("Exiting...")

        # Break terminates the loop
        break

    # ---------------- INVALID CHOICE ----------------
    else:
        print("Invalid Input")