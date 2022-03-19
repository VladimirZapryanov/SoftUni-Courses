from project.student_report_card import StudentReportCard
from unittest import TestCase, main


class StudentReportCardTestCase(TestCase):

    def test_init__when_is_valid__expected_valid_initialized(self):
        student = StudentReportCard("Vlado", 10)

        self.assertEqual("Vlado", student.student_name)
        self.assertEqual(10, student.school_year)
        self.assertEqual({}, student.grades_by_subject)

    def test_init__when_student_name_is_empty_str__expected_to_raise(self):
        with self.assertRaises(ValueError) as context:
            student = StudentReportCard("", 10)
        self.assertEqual("Student Name cannot be an empty string!", str(context.exception))

    def test_init__when_school_year_is_under_one__expected_to_raise(self):
        with self.assertRaises(ValueError) as context:
            student = StudentReportCard("Vlado", 0)
        self.assertEqual("School Year must be between 1 and 12!", str(context.exception))

    def test_init__when_school_year_is_more_than_twelve__expected_to_raise(self):
        with self.assertRaises(ValueError) as context:
            student = StudentReportCard("Vlado", 13)
        self.assertEqual("School Year must be between 1 and 12!", str(context.exception))

    def test_init__when_school_year_is_one__expected_to_set(self):
        student = StudentReportCard("Vlado", 1)
        self.assertEqual(1, student.school_year)

    def test_init__when_school_year_is_twelve__expected_to_set(self):
        student = StudentReportCard("Vlado", 12)
        self.assertEqual(12, student.school_year)

    def test_add_grade__when_subject_not_in_grades_by_subject__expected_to_add_subject_and_grade(self):
        student = StudentReportCard("Vlado", 10)
        student.add_grade("Math", 4.7)

        self.assertTrue("Biology" not in student.grades_by_subject)
        student.add_grade("Biology", 4.4)

        self.assertEqual({'Math': [4.7], "Biology": [4.4]}, student.grades_by_subject)

    def test_add_grade__when_subject_in_grades_by_subject__expected_to_and_grade_to_the_same_subject(self):
        student = StudentReportCard("Vlado", 10)
        student.add_grade("Math", 4.7)
        student.add_grade("Biology", 4.4)
        student.add_grade("Math", 5)

        self.assertEqual({'Math': [4.7, 5], "Biology": [4.4]}, student.grades_by_subject)

    def test_average_grade_by_subject__when_valid__expected_to_return_average_grade_to_every_subject_like_str(self):
        student = StudentReportCard("Vlado", 10)
        student.add_grade("Math", 6)
        student.add_grade("Math", 5)
        student.add_grade("Biology", 4.4)
        student.add_grade("Biology", 5.6)
        expected = "Math: 5.50\nBiology: 5.00"

        self.assertEqual(expected, student.average_grade_by_subject())

    def test_average_grade_for_all_subject__when_valid__expected_to_return_average_grade_to_all_subject_like_str(self):
        student = StudentReportCard("Vlado", 10)
        student.add_grade("Math", 6)
        student.add_grade("Math", 5)
        student.add_grade("Biology", 4.4)
        student.add_grade("Biology", 5.6)
        student.add_grade("Biology", 5.6)
        student.add_grade("History", 3)
        expected_result = f"Average Grade: 4.93"
        result = student.average_grade_for_all_subjects()

        self.assertEqual(expected_result, result)

    def test_repr__when_valid__expected_to_return_str_with_info_for_student(self):
        student = StudentReportCard("Vlado", 10)
        student.add_grade("Math", 4.7)
        student.add_grade("Math", 5)
        student.add_grade("Biology", 4.4)
        student.add_grade("Biology", 4.4)
        result = f"Name: {student.student_name}\n" \
                 f"Year: {student.school_year}\n" \
                 f"----------\n" \
                 f"{student.average_grade_by_subject()}\n" \
                 f"----------\n" \
                 f"{student.average_grade_for_all_subjects()}"

        self.assertEqual(result, student.__repr__())


if __name__ == '__main__':
    main()
