from solution import Person, Developer


def test_check_class_Person():
    person = Person(1, "bal", 23)
    assert person is not None
