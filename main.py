import os 
students = []

def create_folder():  # for folder creation 
    if not os.path.exists("student_data"):
     os.mkdir("student_data")
     

# create_folder()          


def menu():
 print("===== Student Management System =====")    
 menu_options = [
     "Add Student",
     "View Student",
     "Search Student",
     "Update Student",
     "Delete Student",
     "Calculate Grade",
     "Find Topper",
     "Exit",
 
      
 ]
 
 
 for index, options in enumerate(menu_options,start = 1):
    print(f" {index}:{options}")


def main():
    create_folder()

    while True:
        menu()

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_student()

            elif choice == 2:
                view_student()

            elif choice == 3:
                search_student()

            elif choice == 4:
                update_student()

            elif choice == 5:
                delete_student()

            elif choice == 6:
                calculate_grade()

            elif choice == 7:
                find_topper()

            elif choice == 8:
                print("Thank you for using Student Management System.")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 8.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


main()

# def add_student():
#     pass

# def view_student():
#     pass

# def search_student():
#     pass

# def update_student():
#     pass

# def delete_student():
#     pass

# def calculate_grade():
#     pass

# def find_topper():
#     pass