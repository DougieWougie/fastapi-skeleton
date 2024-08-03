from model.example import Example
from errors import Missing, Duplicate


fakes = [
    Example(
        name="J. R. Bob Dobbs",
        country="USA",
        description="Salesman who, in 1953, saw a vision of the god JHVH-1 on a television set he had built.",
    ),
    Example(
        name="Connie Dobbs",
        country="USA",
        description="Wife of a salesman who, in 1953, saw a vision of the god JHVH-1 on a television set he had built.",
    ),
]


def find(name: str) -> Example | None:
    for e in fakes:
        if e.name == name:
            return e
    return None


def check_missing(name: str):
    if not find(name):
        raise Missing(msg=f"Missing example {name}")


def check_duplicate(name: str):
    if find(name):
        raise Duplicate(msg=f"Duplicate example {name}")


def get_all() -> list[Example]:
    """Return all explorers"""
    return fakes


def get_one(name: str) -> Example:
    """Return one example"""
    check_missing(name)
    return find(name)


def create(example: Example) -> Example:
    """Add a example"""
    check_duplicate(example.name)
    return example


def modify(name: str, example: Example) -> Example:
    """Partially modify a example"""
    check_missing(name)
    return example


def delete(name: str) -> None:
    """Delete a example"""
    check_missing(name)
    return None
