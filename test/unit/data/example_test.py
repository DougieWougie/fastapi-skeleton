import os
import pytest
from model.example import Example
from errors import Missing, Duplicate

# -set this before data imports below call data.init
os.environ["CRYPTID_SQLITE_DB"] = ":memory:"
from data import example


@pytest.fixture
def sample() -> Example:
    return Example(name="Pa Tuohy", description="Expectorating example", country="IE")


def test_create(sample):
    resp = example.create(sample)
    assert resp == sample


def test_create_duplicate(sample):
    with pytest.raises(Duplicate):
        _ = example.create(sample)


def test_get_exists(sample):
    resp = example.get_one(sample.name)
    assert resp == sample


def test_get_missing():
    with pytest.raises(Missing):
        _ = example.get_one("Sam Gamgee")


def test_modify(sample):
    sample.country = "CA"
    resp = example.modify(sample.name, sample)
    assert resp == sample


def test_modify_missing():
    bob: Example = Example(name="Bob", description="Bob who?", country="BE")
    with pytest.raises(Missing):
        _ = example.modify(bob.name, bob)


def test_delete(sample):
    resp = example.delete(sample.name)
    assert resp is None


def test_delete_missing(sample):
    with pytest.raises(Missing):
        _ = example.delete(sample.name)
