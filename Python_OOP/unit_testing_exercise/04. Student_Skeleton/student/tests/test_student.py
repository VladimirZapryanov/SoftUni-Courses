from unittest import TestCase, main
from student.project.student import Student


class StudentTests(TestCase):

    def test_init__when_you_have_courses__expect_to_be_initialized_correct(self):
        student = Student("Vlado", {"Python": ["n1", "n2"]})

        self.assertEqual("Vlado", student.name)
        self.assertEqual({"Python": ["n1", "n2"]}, student.courses)

    def test_init__when_without_courses__expect_to_be_initialized_correct(self):
        student = Student("Vlado")

        self.assertEqual("Vlado", student.name)
        self.assertEqual({}, student.courses)

    def test_enroll__when_courses_is_already_exist__expect_to_update_notes_and_return_str(self):
        student = Student("Vlado", {"Python": ["n1", "n2"]})
        result = student.enroll("Python", ["n3", "n4"])

        self.assertTrue("Python" in student.courses)
        self.assertEqual({"Python": ["n1", "n2", "n3", "n4"]}, student.courses)
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll__when_add_new_course_and_notes__expect_to_add_course_and_notes(self):
        student = Student("Vlado", {"Python": ["n1", "n2", "n3"]})

        for idx, command in enumerate(["", "Y"]):
            course_name = f"JavaScript{idx}"
            course_notes = ["js1", "js2"]
            result = student.enroll(course_name, course_notes, command)

            self.assertTrue(course_name in student.courses)
            self.assertEqual(course_notes, student.courses[course_name])
            self.assertEqual("Course and course notes have been added.", result)

    def test_enroll__when_add_new_course_without_notes__expect_to_add_course_withoud_notes(self):
        student = Student("Vlado", {"Python": ["n1", "n2", "n3"]})
        course_name = f"JavaScript"
        course_notes = ["js1", "js2"]
        result = student.enroll(course_name, course_notes, "N")

        self.assertTrue(course_name in student.courses)
        self.assertEqual([], student.courses[course_name])
        self.assertEqual("Course has been added.", result)

    def test_add_notes__when_courses_exist__expect_to_update_notes(self):
        student = Student("Vlado", {"Python": ["n1", "n2"]})
        result = student.add_notes("Python", "n3")

        self.assertEqual({"Python": ["n1", "n2", "n3"]}, student.courses)
        self.assertEqual("Notes have been updated", result)

    def test_add_notes__when_courses_not_exist__expect_to_raise(self):
        student = Student("Vlado", {"Python": ["n1", "n2"]})
        with self.assertRaises(Exception) as context:
            student.add_notes("JavaScript", "n3")
        self.assertEqual("Cannot add notes. Course not found.", str(context.exception))

    def test_leave_course__when_course_exist__expect_to_remove_course(self):
        student = Student("Vlado", {"Python": ["n1", "n2"]})
        result = student.leave_course("Python")
        self.assertEqual("Course has been removed", result)
        self.assertTrue("Python" not in student.courses)

    def test_leave_course__when_course_not_exist__expect_to_raise(self):
        student = Student("Vlado", {"Python": ["n1", "n2"]})
        with self.assertRaises(Exception) as context:
            student.leave_course("JavaScript")
        self.assertEqual("Cannot remove course. Course not found.", str(context.exception))


if __name__ == '__main__':
    main()
