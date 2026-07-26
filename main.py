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

menu()