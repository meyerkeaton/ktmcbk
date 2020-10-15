import pytest
import System
import Student
#student can't check grades of class they are not in
def test_student_wrong_class(grading_system):
    grading_system.login('akend3', '123454321')
    grades = grading_system.usr.check_grades('cloud_computing')
    courses = grading_system.usr.courses
    assert 'cloud_computing' not in courses

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
