import pytest
import System
import Student
#akend3 is not in cloud computing therefore it should fail
def test_student_view_wrong_assignment(grading_system):
    grading_system.login('akend3', '123454321')
    courses = grading_system.usr.courses
    assert 'cloud_computing' in courses
    
@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem