from model.example import Example

# import fake.example as data
import data.example as data


def get_all() -> list[Example]:
    """Get all"""
    return data.get_all()


def get_one(name: str) -> Example | None:
    """Get one if exists"""
    return data.get_one(name)


def create(Example: Example) -> Example:
    """Create"""
    return data.create(Example)


def replace(id, Example: Example) -> Example:
    """Replace an Example"""
    return data.replace(id, Example)


def modify(id, Example: Example) -> Example:
    """Modify an Example"""
    return data.modify(id, Example)


def delete(id, Example: Example) -> bool:
    """Delete an Example"""
    return data.delete(id)
