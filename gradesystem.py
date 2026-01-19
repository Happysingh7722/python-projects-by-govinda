
# student_grades = { }

# def add_student(name, grade):
#     student_grades[name] = grade
    
#     print(f"added {name} with grade {grade}")
    
# def update_student(name, grade):
#     if name in student_grades:
#         student_grades[name] = grade
#         print(f"{name} with markes are updated to {grade}")
    
#     else:
#         print(f"{name} not found in the records!")

# def delete_student(name):
#     if name in student_grades:
#         del student_grades[name]
#         print(f"{name} has been successfully deleted from records.")
#     else:
#         print(f"{name} not found in the records!")

# def display_all_students():
#     if student_grades:
#         for nsame, grade in student_grades.items():
#             print(f"{name} : {grade}")
#     else:
#         print("no student found")


# def main():
#     while Ture:
#         print('\n student grade management system')
#         print('1. Add Student')
#         print('2. update student')
#         print('3. delete student')
#         print('4. view all student')
#         print('5. exit')
        
#         choice = int(input("enter your choice ="))
#         if choice == 1:
#             name = input("enter student name = ")
#             grade = int(input("enter student grade = "))
#             add_student(name, grade)
            
#         elif choice == 2:
#             name = input("enter student name =  ")
#             grade = int(input("enter student grade = "))
#             update_student(name, grade)
        
#         elif choice == 3:   
#             name = input("enter student name =  ")
#             delete_student(name)
        
#         elif choice == 4:
#             display_all_students()
        
#         elif choice == 5:
#             print("exiting the program.")
#             break  
#         else:
#             print("invalid choice! please try again.")
            
            

        
    
        
student_grades = {}

def add_student(name, grade):
    student_grades[name] = grade
    print(f"Added {name} with grade {grade}")

def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name}'s marks updated to {grade}")
    else:
        print(f"{name} not found in records!")

def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} deleted successfully.")
    else:
        print(f"{name} not found in records!")

def display_all_students():
    if student_grades:
        print("\nStudent List:")
        for name, grade in student_grades.items():
            print(f"{name} : {grade}")
    else:
        print("No students found.")

def main():
    while True:
        print("\nStudent Grade Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Exit")

        choice = input("Enter your choice = ")

        if choice == "1":
            name = input("Enter student name = ")
            grade = int(input("Enter student grade = "))
            add_student(name, grade)

        elif choice == "2":
            name = input("Enter student name = ")
            grade = int(input("Enter student grade = "))
            update_student(name, grade)

        elif choice == "3":
            name = input("Enter student name = ")
            delete_student(name)

        elif choice == "4":
            display_all_students()

        elif choice == "5":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

