class Student:
    def __init__(self, stid, stname, attendance, ass_score):
        self.stid = stid
        self.stname = stname
        self.attendance = attendance
        self.ass_score = ass_score
    def check_eligibility(self):
        if self.attendance >= 75 and self.ass_score >= 60:
            return "ELIGIBLE"
        return "NOT ELIGIBLE"
    def generate_report(self):
        print("="*50)
        print("          PLACEMENT ELIGIBILITY REPORT")
        print("="*50)
        print(f"Student ID       : {self.stid}")
        print(f"Student Name     : {self.stname}")
        print(f"Attendance       : {self.attendance}%")
        print(f"Assessment Score : {self.ass_score}")
        print(f"Placement Status : {self.check_eligibility()}")
        print("="*50)
student = Student("JR07", "Anvika", 85, 78)
student.generate_report()