# 2.	Seating Arrangement. 
# You have n students and n chairs in an exam hall. 
# n/3 students are writing Maths, 
# n/3 are writing physics and 
# n/3 are writing chemistry. 

# The n chairs are arranged in two rows, with n/2 in each row. 

# Write an algorithm to make sure no two maths students 
# sit either next/in front/behind of another maths students.

# n students => n/3 each for (MATH, PHYSICS, CHEMISTRY)

# n chairs => 2 rows, with n/2 per row


number_of_students = 4
number_of_chairs = 6

def seating_arrangement(number_of_students, number_of_chairs):
    number_of_rows = 2
    rows = [0] * (number_of_chairs//2)

    #seat sequence of students so it doesn't vilate the 
    #"in front/behind of another maths students" requirement
    student_types = ['Math','Physics','Chemistry']

    # to store total number of student types
    students_writing = []

    #calculating total of all type of students, and storing them
    students_writing = (number_of_students//3) * student_types

    #evaluating "number of students" and "number of chairs"
    if number_of_students <= number_of_chairs:
        for i in range(number_of_rows):
            rows[i] = [0] * (number_of_chairs//2)
        #going over each row
        for i in range(len(rows)):
            #going over each CHAIR allocated to the row 
            for j in range(number_of_chairs//2):
                #checking if we still have students to assign a seat to
                if len(students_writing) > 0:
                    #if on the second row, then check for "not next to" requirement
                    if i > 0 and rows[i][j] == rows[i-1][j]:
                        #if "not next to" requirement is about to be violated, then give seat to next student
                        rows[i][j] = students_writing.pop(1)
                    else:
                        rows[i][j] = students_writing.pop(0)
        print(rows)
    else:
        print('Need more chairs')




seating_arrangement(number_of_students, number_of_chairs)

