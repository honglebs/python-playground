# Grading Students 

# Every student receives a grade in the inclusive range from 0 to 100.
# Any grade less than 40 is a failing grade.

# ROUNDING RULES
# if the difference between the grade and the next multiple of 5 is less than 3,
# round grade up to the next multiple of 5

# if the value of the grade is less than 38, 
# no rounding occurs as the result will still be a failing grade


def gradingStudents(grades):
    
    # create empty list to store rounded grades
    rounded_grades = []

    # iterate for each grade in list of grades
    for grade in grades:
        # if grade is less than 38, append it to the list of rounded_grades
        if grade < 38:
            rounded_grades.append(grade)
        else:
            # otherwise, calc the next multiple of 5 greater than the grade
            next_multiple_of_5 = ((grade // 5) + 1) * 5
            
            # if the difference between the next multiple of 5 & grade less than 3, append 
            if next_multiple_of_5 - grade < 3:
                rounded_grades.append(next_multiple_of_5)
            else:
                # otherwise, append the original grade to list of rounded_grades
                rounded_grades.append(grade)

    # return list of rounded_grades            
    return rounded_grades
    







