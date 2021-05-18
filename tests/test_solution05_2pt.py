from solution import Developer


def test_check_repr_Developer():
    dev = Developer(1, "bal", 23, 1000.0, "python")
    strDev = dev.__repr__()
    assert strDev == "Dev(id: 1, name: bal, age: 23, salary: 1000.0, language: python)"
