class Person:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def __repr__(self):
        strPerson = f"Person(id:{self.id}, name:{self.name}, age:{self.age})"
        return strPerson

class Developer:
    def __init__(self):
        pass

class Roster:
    def __init__(self):
        pass
