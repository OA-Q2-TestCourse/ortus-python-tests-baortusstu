from solution import Person


def test_check_repr_Person():
    person = Person(1, "bal", 23)
    strPerson = person.__repr__()
    assert strPerson == "Person(id: 1, name: bal, age: 23)"
