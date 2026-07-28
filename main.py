import os
 
students = [
    {
        "id": 101,
        "name": "Kamal",
        "age": 22,
        "course": "Python",
        "marks": 95
    },
    {
        "id": 102,
        "name": "Ali",
        "age": 20,
        "course": "Java",
        "marks": 85
    },
    {
        "id": 103,
        "name": "Ali kumar",
        "age": 20,
        "course": "Javascript",
        "marks": 85
    }
]

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





def get_student_by_id(Id):
    for student in students:
        if student["id"] == Id:
            return student

    return None
    
def add_student():   
 while True:
    Id = int(input("Enter student id: "))
    found = get_student_by_id(Id) 
     
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
   

def view_student():
    if not students:
        print("--------------------------")
        print("List khali aa mama")
        print("--------------------------")
        return
    if students:
        for index, student in enumerate(students, start=1):
            print("--------------------------")
            print(f" Student {index}")
            print(f"ID : {student['id']}")
            print(f"Name : {student['name']}")
            print(f"Age : {student['age']}")
            print(f"Course : {student['course']}")
            print(f"Marks : {student['marks']}")
            print("--------------------------")




def search_student():
    Id = int(input("Enter student id: "))
    found = get_student_by_id(Id) 
    
    if found:
     print("-----------------------")
     print(f"ID     : {found['id']}")
     print(f"Name   : {found['name']}")
     print(f"Age    : {found['age']}")
     print(f"Course : {found['course']}")
     print(f"Marks  : {found['marks']}")
     print("-----------------------")
     
    else:
        print("This student is not available")    



def update_student():
    Id = int(input("Enter student id: "))
    student = get_student_by_id(Id) 
     
    if student:
      
     name = input("Enter new name : ")
     age = int(input("Enter new age : "))
     course = input("Enter new course : ")
     marks = float(input("Enter new marks : "))
     
     student["name"] = name
     student["age"] = age
     student["course"] = course
     student["marks"] = marks
    
     print("-----------------------")
     print(f"ID     : {student['id']}")
     print(f"Name   : {student['name']}")
     print(f"Age    : {student['age']}")
     print(f"Course : {student['course']}")
     print(f"Marks  : {student['marks']}")
     print("-----------------------")
     
     print("Student updated succesfully")
  
    else:
        print("This student is not available")
        
    


         
def delete_student():
    Id = int(input("Enter student id: "))

    student = get_student_by_id(Id)

    if not student:
        print("Student not found.")
        return

    confirm = input("Are you sure? (Y/N): ").lower()

    if confirm == "y":
        students.remove(student)
        print("Student deleted successfully.")

    elif confirm == "n":
        print("Deletion cancelled.")

    else:
        print("Invalid input.")    
        
 
 

def calculate_grade(marks):

    if marks >= 90:
        return "A+"

    elif marks >= 80:
        return "A"

    elif marks >= 70:
        return "B"

    elif marks >= 60:
        return "C"

    elif marks >= 50:
        return "D"

    else:
        return "F"


def student_grade():
    Id = int(input("Enter student id: "))

    student = get_student_by_id(Id)

    if not student:
        print("Student not found.")
        return

    grade = calculate_grade(student["marks"])

    print("-----------------------")
    print(f"ID     : {student['id']}")
    print(f"Name   : {student['name']}")
    print(f"Marks  : {student['marks']}")
    print(f"Grade  : {grade}")
    print("-----------------------")
    
  
  

def find_topper():
    if not students:
        print("--------------------------")
        print("No students available.")
        print("--------------------------")
        return

    topper = students[0]

    for student in students:
        if student["marks"] > topper["marks"]:
            topper = student

    grade = calculate_grade(topper["marks"])

    print("--------------------------")
    print("Topper Details")
    print("--------------------------")
    print(f"ID     : {topper['id']}")
    print(f"Name   : {topper['name']}")
    print(f"Age    : {topper['age']}")
    print(f"Course : {topper['course']}")
    print(f"Marks  : {topper['marks']}")
    print(f"Grade  : {grade}")
    print("--------------------------")
                

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
                student_grade()

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

