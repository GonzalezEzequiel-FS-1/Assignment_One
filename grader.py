class MyGrader:
    def grade_student(self):
        # Getting Student's name
        name = input("What's your name?\n")
        # If no name, return error
        if name == "":
            return 'Please answer all questions.'
        # Then get the class Name
        class_name = input(f"Hello {name}, can I get the assignment's name?\n")
        # If no class name return error
        if class_name == "":
            return 'Please answer all questions.'
        try:
            # A try block to get grade as a float
            grade = round(float(input(f"Now, let's get your score in {class_name}.\n")), 1)

        except ValueError:
            return 'Please enter a valid numeric grade.'

        # Now we use a conditional to return the grade and message depending on the student's grade
        if 100 >= grade >= 90:
            letter_grade = 'A'
            passing = True
            message = 'you have met all'
        elif 90 > grade >= 80:
            letter_grade = 'B'
            message = 'you have met most'
            passing = True
        elif 80 > grade >= 70:
            letter_grade = 'C'
            message = 'you have not met most'
            passing = True
        elif 70 > grade >= 60:
            letter_grade = 'D'
            message = 'you have missed most'
            passing = False
        elif 60 >= grade >= 0:
            letter_grade = 'F'
            message = 'you have missed all'
            passing = False
        else:
            # Catch values above or under the specified threshold <  0 and > 100
            return f'{name}, Please enter a numeric grade with a value between 0 and 100'

        # Dynamic Greeting depending on passing status
        greeting = "Congratulations" if passing else "Sorry"

        return f'{greeting} {name}, since your score for {class_name} is {grade}, you got a letter grade of {letter_grade}.\n{name}, {message} of the requirements for this class.'

# Instantiate ** COMMENTED OUT FOR TESTING **
#testGrader = MyGrader()

# Print ** COMMENTED OUT FOR TESTING ***
#print(testGrader.grade_student())
