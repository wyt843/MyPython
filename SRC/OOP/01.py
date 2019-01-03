class Student():
    pass
mingyue = Student()

class PythonStudent():
    name = None
    age = 18
    course = "Python"

    def doHomework(self):
        print "i'm doning homework"
        return None
stu1 = PythonStudent()
print stu1.name
print stu1.age
stu1.doHomework()
for item in PythonStudent.__dict__:
    print '{:20}'.format(item)