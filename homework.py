# class Homework:
#    def _init_(self, surname, name, description, complexity, status):
#        self.surname = surname
#        self.name = name
#        self.description = description
#        self.complexity = complexity
#        self.status = status
#        self.grade = 0
#
#    def _str_(self):
#        return f"{self.surname}, {self.name}, {self.description}, {self.complexity}, {self.status}"
#



class Homework:

    def __init__(self, name, description, complexity, status):
        self.name = name
        self.description = description
        self.complexity = complexity
        self.status = status
        self.grade = 0

    def __str__(self):
        return f"{self.name}, {self.description}, {self.complexity}, {self.status}"


class Student:
    def __init__(self, surname, name, age, course):
        self.surname = surname
        self.name = name
        self.age = age
        self.avarage_grade = 0
        self.course = course
        self.homeworks = []

    def __str__(self):
        ret = f"surname: {self.surname}, name:{self.name}, age: {self.age}, grade: {self.avarage_grade}, course: {self.course}\n"
        ret = ret + "Homeworks:\n"
        for i in self.homeworks:
            ret = ret + "\t" + str(i) + "\n"
        return ret

    def add_homework(self, homework):
        self.homeworks.append(homework)


def show_students(students):
    for s in students:
        print(s)


def sort_by_name(students):
    return sorted(students, key=lambda s: s.name)

def sort_by_age(students):
    return sorted(students, key=lambda s: s.age)


def sort_by_grade(students):
    return sorted(students, key=lambda s: s.avarage_grade, reverse=True)

def sort_by_surname(students):
    return sorted(students, key=lambda s: s.surname)

students = [
    Student("Smith", "Lena", 18, "C++"),
    Student("Williams", "Nike", 26, "Python"),
    Student("Brown", "Peter", 25, "Java"),
    Student("Smith", "John", 15, "Python"),
    Student("Wilson", "Peter", 17, "C++")
]
studentst = list(zip(students))
print(str(studentst))
homeworks = [
    Homework("Homework 1", "Description 1", 2, False),
    Homework("Homework 2", "Description 2", 5, False)
]

print("Initial")
show_students(students)
print("Sorted by name")
show_students(sort_by_name(students))
print("Sorted by surname")
show_students(sort_by_surname(students))
print("Sorted by age")
show_students(sort_by_age(students))
print("Sorted by grade")
show_students(sort_by_grade(students))
#
#
# class Homework:

#
#     def __init__(self, name, description, complexity, status):
#
#         self.name = name
#         self.description = description
#         self.complexity = complexity
#         self.status = status
#         self.grade = 0
#
#     def __str__(self):
#         return f"{self.name}, {self.description}, {self.complexity}, {self.status}"
#
#
# class Student:
#     def __init__(self, name, age, subscribed_course):
#         self.name = name
#         self.age = age
#         self.avarage_grade = 0
#         self.subscribed_course = subscribed_course
#         self.homeworks = []
#
#     def __str__(self):
#         ret = f"{self.name}, age: {self.age}, grade: {self.avarage_grade}, course: {self.subscribed_course}\n"
#         ret = ret + "Homeworks:\n"
#         for h in self.homeworks:
#             ret = ret + "\t" + str(h) + "\n"
#         return ret
#
#     def add_homework(self, homework):
#         self.homeworks.append(homework)
#
#
#
# def show_students(students):
#     for s in students:
#         print(s)
#
#
# def sort_by_age(students):
#     return sorted(students, key=lambda s: s.age)
#
#
# def sort_by_grade(students):
#     return sorted(students, key=lambda s: s.avarage_grade, reverse=True)
#
#
# students = [
#     Student("Student 1", 12, "Python")
#     , Student("Student 2", 16, "Python")
#     , Student("Student 3", 15, "Python")
#     , Student("Student 4", 14, "Python")
#     , Student("Student 5", 10, "Python")
# ]
#
# homeworks = [
#     Homework("Homework 1", "Description 1", 2, False)
#     , Homework("Homework 2", "Description 2", 5, False)
# ]
#
# print("Initial")
# show_students(students)
# print("Sorted by age")
# show_students(sort_by_age(students))
# print("Sorted by grade")
# show_students(sort_by_grade(students))