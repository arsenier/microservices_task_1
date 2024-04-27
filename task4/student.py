class Student:
    def __init__(self, name, age, group, avg_grade):
        self.name = name
        self.age = age
        self.group = group
        self.avg_grade = avg_grade

        self.sch_grade_max = 5
        self.sch_threshold = 4
        self.sch_low = 4000
        self.sch_high = 6000
    
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def __str__(self):
        return "Name: " + str(self.get_name()) +\
        ", age: " + str(self.get_age()) +\
        ", scholarship: " + str(self.get_scholarship())
    
    def get_scholarship(self):
        if self.avg_grade == self.sch_grade_max:
            return self.sch_high
        elif self.avg_grade > self.sch_threshold:
            return self.sch_low
        else:
            return 0
        
    def compare_scholarship(self, obj):
        return self.get_scholarship() > obj.get_scholarship()
    
class Aspirant(Student):
    def __init__(self, name, age, group, avg_grade, thesis):
        super().__init__(name, age, group, avg_grade)
        self.thesis = thesis
        self.sch_low = 6000
        self.sch_high = 8000

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

print(vasya.compare_scholarship(petya))

print(petya)
petya.avg_grade = 4
print(petya)

