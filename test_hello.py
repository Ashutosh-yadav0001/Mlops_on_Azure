from hello import more_hello

def  test_more_hello():
    assert more_hello() == "Hello again!"

def test_more_hello_not_equal():
    assert more_hello() == "bye"
    "
    
