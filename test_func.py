from func import catsay, dogsay, cowsay

def test_catsay():
    assert catsay() == "meow!"

def test_dogsay():
    assert dogsay() == "woof!"

def test_cowsay():
    assert cowsay() == "moo!"
