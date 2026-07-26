import os 
students = []

def create_folder():
    if not os.path.exists("student_data"):
     os.mkdir("student_data")
     

create_folder()          