from fastapi import HTTPException
import pytest
import os

os.environ["EXAMPLE_UNIT_TEST"] = "true"
from model.example import Example
from web import example
from errors import Missing, Duplicate


@pytest.fixture
def sample() -> Example:
    return Example(
        name='J. R. "Bob" Dobbs',
        country="USA",
        description="Salesman who, in 1953, saw a vision of the god JHVH-1 on a television set he had built.",
    )


@pytest.fixture
def fakes() -> list[Example]:
    return example.get_all()


def assert_duplicate(exc):
    assert exc.value.status_code == 404
    assert "Duplicate" in exc.value.msg


def assert_missing(exc):
    assert exc.value.status_code == 404
    assert "Missing" in exc.value.msg


def test_create(sample):
    assert example.create(sample) == sample


def test_create_duplicate(fakes):
    with pytest.raises(HTTPException) as exc:
        resp = example.create(fakes[0])
        assert_duplicate(exc)


def test_get_one(fakes):
    assert example.get_one(fakes[0].name) == fakes[0]


def test_get_one_missing():
    with pytest.raises(HTTPException) as exc:
        resp = example.get_one("Buffy")
        assert_missing(exc)


def test_modify(fakes):
    assert example.modify(fakes[0].name, fakes[0]) == fakes[0]


def test_modify_missing(sample):
    with pytest.raises(HTTPException) as exc:
        resp = example.modify(sample.name, sample)
        assert_missing(exc)


def test_delete(fakes):
    assert example.delete(fakes[0].name) is None


def test_delete_missing(sample):
    with pytest.raises(HTTPException) as exc:
        resp = example.delete("Wally")
        assert_missing(exc)
