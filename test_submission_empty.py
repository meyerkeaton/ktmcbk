import pytest
import System
import Student

def test_submission_empty(grading_system):
    grading_system.login('akend3', '123454321')
    grading_system.usr.submit_assignment('comp_sci', 'assignment2', '', '2/9/20')
    grading_system.reload_data()
    assignment = grading_system.usr.courses['comp_sci']['assignment2']
    assert assignment['submission'] != '' 
 
@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem