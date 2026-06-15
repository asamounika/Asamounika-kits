class course:
    def course_fee(self):
        print("Basic Course Fee is:5000")
class AdvancedCourse(course):
    def course_fee(self):
        print("Advanced Course Fee is: 12000")
ac=AdvancedCourse()
ac.course_fee()
c=course()
c.course_fee()