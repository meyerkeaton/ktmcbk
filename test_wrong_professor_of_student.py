import pytest
import System
import Student

# goggins is not professor of cloud computing therefore it should fail
def test_wrong_professor_of_student(grading_system):
    grading_system.login('goggins', 'augurrox')
    grades = grading_system.usr.check_grades('yted91', 'cloud_computing')
    assert grades == []
 
@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem