from model.example import Example

# Fake data
_example = [
    Example(
        name='J. R. "Bob" Dobbs',
        country="USA",
        description="Salesman who, in 1953, saw a vision of the god JHVH-1 on a television set he had built.",
    ),
]


def get_all() -> list[Example]:
    """Return all Examples"""
    return _example


def get_one(name: str) -> Example | None:
    for _Example in _example:
        if _Example.name == name:
            return _Example
    return None


def create(Example: Example) -> Example:
    """Add an Example"""
    return Example


def modify(Example: Example) -> Example:
    """Partially modify an Example"""
    return Example


def replace(Example: Example) -> Example:
    """Completely replace an Example"""
    return Example


def delete(name: str) -> bool:
    """Delete an Example; return None if it existed"""
    return None
