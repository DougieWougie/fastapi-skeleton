from model.example import Example
from service import Example as code

sample = Example(
    name='J. R. "Bob" Dobbs',
    country="USA",
    description="Salesman who, in 1953, saw a vision of the god JHVH-1 on a television set he had built.",
)


def test_create():
    resp = code.create(sample)
    assert resp == sample


def test_get_exists():
    resp = code.get_one('J. R. "Bob" Dobbs')
    assert resp == sample


def test_get_missing():
    resp = code.get_one("Connie Dobbs")
    assert resp is None
