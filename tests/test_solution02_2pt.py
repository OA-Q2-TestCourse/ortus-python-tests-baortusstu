from solution import Person, Developer


def test_check_class_Developer():
    developer = Developer(1, "bal", 23, 1000.0, "python")
    assert developer is not None
