class Student:
    def placement_status(self):
        print("Placement Eligibility: Assessment Score Above 60")
class AdvancedStudent(Student):
    def placement_status(self):
        print("Placement Eligibility: Assessment Score Above 80")
student = Student()
student.placement_status()
student= AdvancedStudent()
student.placement_status()