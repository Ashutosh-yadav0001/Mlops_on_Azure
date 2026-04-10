from hello import more_hello, more_goodbye


def test_more_hello():
    assert more_hello() == "Hello again!"


def test_more_goodbye():
    assert more_goodbye() == "Goodbye again!"
