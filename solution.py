class Person:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def __repr__(self):
        strPerson = f"Person(id: {self.id}, name: {self.name}, age: {self.age})"
        return strPerson

class Developer(Person):
    def __init__(self, id, name, age, salary, language):
        super().__init__(id, name, age)
        self.salary = salary
        self.language = language

    def __repr__(self):
        strDev = (
            f"Dev(id: {self.id}, name: {self.name}, "
            +f"age: {self.age}, salary: {self.salary}, language: {self.language})"
        )
        return strDev


class Roster:
    def __init__(self):
        pass
