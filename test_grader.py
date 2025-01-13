# We start by importing unittest
import unittest
# Then importing patch from unittest.mock
from unittest.mock import patch
# Now, from grader, let's bring the MyGrader class
from grader import MyGrader
# Let's import the logging library
import logging
# Let's import the re module, so we can search through RegExes
import re

# Logging Results

logging.basicConfig(
    level=logging.INFO,
    filename='graderLog.log',
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w'
)


# Let's start Testing!!!
class TestGrader(unittest.TestCase):

    # We use @patch to provide the Mock inputs
    @patch('builtins.input', side_effect=['Zeke', "AIS", "95"])
    # Now, we define the test
    def test_student_A(self, mock_input):
        # Instantiate Class
        grader = MyGrader()
        # We call the method to get the output
        result = grader.grade_student()
        # Then we provide the expected output
        expected_output = (
            'Congratulations Zeke, since your score for AIS is 95.0, you got a letter grade of A.\nZeke, you have met all of the requirements for this class.'
        )
        # I'm setting the passing grade for each category to use in testing
        passing_grade = 90
        # Let's also set the maximum grade for the category
        top_grade = 100

        # by using re, we create a regex to capture the score from the user's response
        match = re.search(r"score for \S+ is (\d+\.\d+)", result)
        if match:
            grade = float(match.group(1))
        else:
            grade = None
        try:
            # Lets use assertTrue() in the code I assigned a True or false value to
            # dynamically change the greeting, let's use the greeting to call assertTrue()
            self.assertTrue("Congratulations" in result)
            logging.info(f'Assert True Passed in {self}')

            # Now we are using assertEqual to compare the result and expected output
            self.assertEqual(result, expected_output)
            logging.info(f'Assert Equal Test Passed at: {self}')

            # Similarly we can use the assertMultiLineEqual to test our code:
            self.assertMultiLineEqual(result, expected_output)
            logging.info(f'Assert Multi Line Test Passed at: {self}, comparing: {result} with: {expected_output}')

            # We can use assertGreaterEqual to check if the student's grade is higher than the passing grade, therefore
            # the grade reported would be the correct one:
            self.assertGreaterEqual(grade, passing_grade)

            # Now, we are using assertLessEqual to check if the grade falls inside the correct range, in conjunction
            # with assertGreaterEqual
            self.assertLessEqual(grade, top_grade)
            logging.info(f'"A" Grade check passed for {grade} >= {passing_grade} and {grade} <= {top_grade}')

            # Now, we capture the AssertionError if any
        except AssertionError as e:
            logging.error(f'Test Failed {e}')
            raise

    @patch('builtins.input', side_effect=['', 'AIS', '95'])
    # Empty name, class name = AIS, grade = 95
    def test_empty_name(self, mock_input):
        try:
            grader = MyGrader()
            result = grader.grade_student()
            # This is not the one
            self.assertEqual(result, 'Please answer all questions.')
        except AssertionError as e:
            logging.error(f'Test Failed {e}')
            raise

    @patch('builtins.input', side_effect=['Zeke', '', '95'])
    # Name = Zeke, empty class name, grade = 95
    def test_empty_class_name(self, mock_input):
        try:
            grader = MyGrader()
            result = grader.grade_student()
            #This is not the one
            self.assertEqual(result, 'Please answer all questions.')
        except AssertionError as e:
            logging.error(f'Test Failed {e}')
            raise

    @patch('builtins.input', side_effect=['Zeke', 'Math 101', "abc"])
    def test_invalid_grade(self, mock_input):
        grader = MyGrader()
        result = grader.grade_student()
        try:
            self.assertEqual(result, 'Please enter a valid numeric grade.')
        except AssertionError as e:
            logging.error(f'Test Failed {e}')
            raise

    @patch('builtins.input', side_effect=['Zeke', 'AIS', '95.5'])
    def test_valid_rounded_grade(self, mock_input):
        grader = MyGrader()
        result = grader.grade_student()
        expected_output = (
            'Congratulations Zeke, since your score for AIS is 95.5, you got a letter grade of A.\nZeke, you have met all of the requirements for this class.'
        )
        try:
            self.assertEqual(result, expected_output)
            logging.info(f'Testing Rounded output')
        except AssertionError as e:
            logging.error(f'Test Failed {e}')
            raise

    @patch('builtins.input', side_effect=['Zeke', 'AIS', ''])
    def test_empty_grade(self, mock_input):
        try:
            grader = MyGrader()
            result = grader.grade_student()
            self.assertEqual(result, 'Please enter a valid numeric grade.')
            logging.info(f'Empty Grade Test Passed')
        except AssertionError as e:
            logging.error(f'Test Failed {e}')
    @patch('builtins.input', side_effect=[""])
    def test_empty_response(self, mock_input):
        # Testing a complete lack of input from the user:
        try:
            grader = MyGrader()

            self.assertRaises(ValueError)
            grader.grade_student()
            logging.info(f'Empty response Test Passed')
        except AssertionError as e:
            logging.critical(f'No Input From User: {e}')

    # NOTE, since the following tests will be mostly repetitions testing for the individual text, I will not include the
    # comments unless needed, in an effort to reduce clutter and make it more legible
    @patch('builtins.input', side_effect=['Zeke', "AIS", "89.9"])
    def test_edge_B(self, mock_input):

        grader = MyGrader()
        result = grader.grade_student()
        expected_output = (
            'Congratulations Zeke, since your score for AIS is 89.9, you got a letter grade of B.\nZeke, you have met most of the requirements for this class.'
        )

        passing_grade = 80
        top_grade = 89.9
        match = re.search(r"score for \S+ is (\d+\.\d+)", result)
        if match:
            grade = float(match.group(1))
        else:
            grade = None
        try:
            self.assertEqual(result, expected_output)
            logging.info(f'Assert Equal Test Passed at: {self}')
            self.assertGreaterEqual(grade, passing_grade)
            logging.info(f'Edge "B" Grade check passed for {grade} >= {passing_grade}')
            self.assertLessEqual(grade, top_grade)
            logging.info(f'"B" Grade check passed for {grade} >= {passing_grade} and {grade} <= {top_grade}')
        except AssertionError as e:
            logging.error(f'Test Failed {e}')
            raise

        try:
            self.assertTrue("Congratulations" in result)
            logging.info(f'Assert True Passed in {self}')
        except AssertionError as e:
            logging.error(f'Assert True at {self} failed with error: {e}')

    @patch('builtins.input', side_effect=['Zeke', "AIS", "85"])
    def test_student_B(self, mock_input):
        grader = MyGrader()
        result = grader.grade_student()
        expected_output = (
            'Congratulations Zeke, since your score for AIS is 85.0, you got a letter grade of B.\nZeke, you have met most of the requirements for this class.'
        )

        passing_grade = 80
        top_grade = 89.9
        match = re.search(r"score for \S+ is (\d+\.\d+)", result)
        if match:
            grade = float(match.group(1))
            logging.info(f'Logging grade: {grade}')
        else:
            grade = None

        try:
            self.assertEqual(result, expected_output)
            logging.info(f'Assert Equal Test Passed at: {self}')
            self.assertGreaterEqual(grade, passing_grade)
            self.assertLessEqual(grade, top_grade)
            logging.info(f'"C" Grade check passed for {grade} >= {passing_grade} and {grade} <= {top_grade}')
        except AssertionError as e:
            logging.error(f'Test Failed {e}')
            raise
        try:
            self.assertTrue("Congratulations" in result)
            logging.info(f'Assert True Passed in {self}')
        except AssertionError as e:
            logging.error(f'Assert True at {self} failed with error: {e}')

    @patch('builtins.input', side_effect=['Zeke', "AIS", "75"])
    def test_student_C(self, mock_input):
        grader = MyGrader()
        result = grader.grade_student()
        expected_output = (
            'Congratulations Zeke, since your score for AIS is 75.0, you got a letter grade of C.\nZeke, you have not met most of the requirements for this class.'
        )
        passing_grade = 70
        top_grade = 79.9

        match = re.search(r"score for \S+ is (\d+\.\d+)", result)
        if match:
            grade = float(match.group(1))
        else:
            grade = None
        try:
            self.assertEqual(result, expected_output)
            logging.info(f'Assert Equal Test Passed at: {self}')
            self.assertGreaterEqual(grade, passing_grade)
            self.assertLessEqual(grade, top_grade)
            logging.info(f'"C" Grade check passed for {grade} >= {passing_grade} and {grade} <= {top_grade}')
        except AssertionError as e:
            logging.error(f'Test Failed: {e}')
            raise

        try:
            self.assertTrue("Congratulations" in result)
            logging.info(f'Assert True Passed in {self}')
        except AssertionError as e:
            logging.error(f'Assert True at {self} failed with error: {e}')

    @patch('builtins.input', side_effect=['Zeke', "AIS", "65"])
    def test_student_D(self, mock_input):
        grader = MyGrader()
        result = grader.grade_student()

        expected_output = (
            'Sorry Zeke, since your score for AIS is 65.0, you got a letter grade of D.\nZeke, you have missed most of the requirements for this class.'
        )

        passing_grade = 60
        top_grade = 69.9
        match = re.search(r"score for \S+ is (\d+\.\d+)", result)
        if match:
            grade = float(match.group(1))
        else:
            grade = None
        try:
            self.assertEqual(result, expected_output)
            logging.info(f'Assert Equal Test Passed at: {self}')
            self.assertGreaterEqual(grade, passing_grade)
            self.assertLessEqual(grade, top_grade)
            logging.info(f'"D" Grade check passed for {grade} >= {passing_grade} and {grade} <= {top_grade}')
        except AssertionError as e:
            logging.error(f'Assert Equal Test Failed: {e}')
            raise
        try:
            # NOTE THAT HERE WE LOOK FOR SORRY NOT CONGRATULATIONS
            # Sorry being the False analogue
            self.assertTrue("Sorry" in result)
            logging.info(f'Assert True Passed in {self}')
        except AssertionError as e:
            logging.error(f'Assert True at {self} failed with error: {e}')

    @patch('builtins.input', side_effect=['Zeke', "AIS", "10"])
    def test_student_F(self, mock_input):
        grader = MyGrader()
        result = grader.grade_student()

        expected_output = (
            'Sorry Zeke, since your score for AIS is 10.0, you got a letter grade of F.\nZeke, you have missed all of the requirements for this class.'
        )

        passing_grade = 59
        match = re.search(r"score for \S+ is (\d+\.\d+)", result)
        if match:
            grade = float(match.group(1))
        else:
            grade = None

        try:
            self.assertEqual(result, expected_output)
            # NOTE: HERE WE LOOK FOR A NUMBER LOWER THAN 59 to assign the "F" Grade.
            # We test for < 0 on our edge cases, so it would be redundant to include it here.
            self.assertLessEqual(grade, passing_grade)
            logging.info(f'"F" Grade check passed for {grade} >= {passing_grade}')
        except AssertionError as e:
            logging.error(f'Test Failed: {e}')
        try:

            self.assertTrue("Sorry" in result)
            logging.info(f'Assert True Passed in {self}')
        except AssertionError as e:
            logging.error(f'Assert True at {self} failed with error: {e}')

# "EDGE CASES"
    @patch('builtins.input', side_effect=['Zeke', "AIS", "10000"])
    def test_its_over_one_hundred(self, mock_input):
        # Instantiate Class
        grader = MyGrader()
        # We call the method to get the output
        result = grader.grade_student()
        # Then we provide the expected output
        expected_output = (
            'Zeke, Please enter a numeric grade with a value between 0 and 100'
        )
        match = re.search(r"score for \S+ is (\d+\.\d+)", result)
        if match:
            grade = float(match.group(1))
        else:
            grade = None

        try:
            # Now we are using assertEqual to compare the result and expected output
            self.assertEqual(result, expected_output)
            logging.info(f'Checking edge case passed: {expected_output}, provided {grade}')
        except AssertionError as e:
            logging.error(f'Test Failed: {e}')

    @patch('builtins.input', side_effect=['Zeke', "AIS", -1])
    def test_the_test_is_a_lie(self, mock_input):
        grader = MyGrader()
        result = grader.grade_student()
        expected_output = (
            'Zeke, Please enter a numeric grade with a value between 0 and 100'
        )

        match = re.search(r"score for \S+ is (\d+\.\d+)", result)
        if match:
            grade = float(match.group(1))
        else:
            grade = None

        try:
            self.assertEqual(result, expected_output)
            logging.info(f'Checking edge case passed: {expected_output}, provided {grade}')
        except AssertionError as e:
            logging.error(f'Test Failed: {e}')


if __name__ == "__main__":
    logging.info("Starting Tests...")
    unittest.main()
    logging.info("All tests completed.")
