import os
from model.example import Example

if os.getenv("EXAMPLE_UNIT_TEST"):
    from fake import example as data
else:
    from data import example as data


def get_all() -> list[Example]:
    return data.get_all()


def get_one(name: str) -> Example:
    return data.get_one(name)


def create(example: Example) -> Example:
    return data.create(example)


def modify(name: str, example: Example) -> Example:
    return data.modify(name, example)


def delete(name: str):
    return data.delete(name)
