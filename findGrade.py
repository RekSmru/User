    # Student Grade Calculator

try:
    # Taking user input
    marks = float(input("Enter your marks (0-100): "))

    # Validate the marks are within a plausible range (0-100)
    if 0 <= marks <= 100:

        # Grade classification

    # grade = A: 90 and above
        if marks >= 90:
            grade = "A"

    # grade = B: between 80 and 89
        elif marks >= 80:
            grade = "B"

    # grade = C: between 70 and 79
        elif marks >= 70:
            grade = "C"

    # grade = D: between 60 and 69
        elif marks >= 60:
            grade = "D"

    # grade = F: below 60
        else:
            grade = "F"
        print(f"Your grade is: {grade}")

    # Out-of-range error  
    else:
        print("Error: Marks must be between 0 and 100.")

    # Invalid Input
except ValueError:
    print("Invalid input. Please enter a numeric value.")