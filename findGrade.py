    # Students Grade Calculator

try:
    # Taking user input
    score = int(input ("Please enter your score : "))

    # Validate the scores are within a possible range(0-100)
    if 0 <= score <= 100:

        # Grade classification

    # student_grade = A: 90 and above
        if score >= 90:
           student_grade = "A"

    # student_grade = B: between 80 and 89
        elif score >= 80:
            student_grade = "B"

    # student_grade = C: between 70 and 79
        elif score >= 70:
            student_grade = "C"

    # student_grade = D: between 60 and 69
        elif score >= 60:
            student_grade = "D"

    # student_grade = F: below 60
        else:
            student_grade = "F"

        print(f"Your grade is: {student_grade}")

    # Out-of-range error  
    else:
        print("Error: Your score must be between 0 and 100.")

    # Invalid Input
except ValueError:
    print("Invalid input. Please enter a numeric value.")
