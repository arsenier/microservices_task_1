class Student:
    def __init__(self, name, age, group, avg_grade):
        self.name = name
        self.age = age
        self.group = group
        self.avg_grade = avg_grade
    
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def __str__(self):
        return "Name: " + str(self.getName()) +\
        ", age: " + str(self.getAge()) +\
        ", scholarship: " + str(self.getScholarship())
        
    def getScholarship(self):
        if self.avg_grade == 5:
            return 6000
        elif self.avg_grade > 4:
            return 4000
        else:
            return 0
        
    def compareScholarship(self, obj):
        return self.getScholarship() > obj.getScholarship()
    
class Aspirant(Student):
    def __init__(self, name, age, group, avg_grade, thesis):
        super().__init__(name, age, group, avg_grade)
        self.thesis = thesis
    
    def getScholarship(self):
        if self.avg_grade == 5:
            return 8000
        elif self.avg_grade > 4:
            return 6000
        else:
            return 0

    def __str__(self):
        return super().__str__() + ", thesis: " + str(self.thesis)

vasya = Student("Vasya", 25, 270403, 5)
print(vasya)
vasya.avg_grade = 4.5
print(vasya)
vasya.avg_grade = 4
print(vasya)

petya = Aspirant("Petya", 213, 270403, 5, "THESIS NAME")
print(petya)
petya.avg_grade = 4.5

print(vasya.compareScholarship(petya))

print(petya)
petya.avg_grade = 4
print(petya)

