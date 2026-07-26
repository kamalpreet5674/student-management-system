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


# students = [
#     {"id":101, "name":"kamal", "age":22, "marks":90},
#     {"id":102, "name":"kamalpreet", "age":26, "marks":90},
# ]


def check_student_id(Id):
    for student in students:
        if student["id"] == Id:
            
            return True
        

    return False
    
def add_student():

        
     
 while True:
    Id = int(input("Enter student id: "))
    found = check_student_id(Id) 
     
    if found:
        print("This student is already avaliable")
        continue
    
    if not found:
      name = input("Enter the name of student:")
      age = int(input("Enter the age of student:"))
      course = input("Enter the couse of student:")
      marks = float(input("Enter the marks of student:"))
      student = {
         "id": Id,
         "name": name,
         "age": age,
         "course": course,
         "marks": marks
     }
      students.append(student)
      print(students)
      print("Student added successfully")
      return
   




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


if __name__ == "__main__":
    main()

