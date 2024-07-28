from fastapi import APIRouter

import service.example as service
from model.example import Example

# Define router
router = APIRouter(prefix="/example")

# Define actions using decorators, remembering to specify
# the terminated and non-terminated endpoint.

@router.get("")
@router.get("/")
def get_all() -> list[Example]:
    """Return all"""
    return service.get_all()


@router.get("/{name}")
def get_one(name) -> Example | None:
    return service.get_one(name=name)


@router.post("")
@router.post("/")
def create(Example: Example) -> Example:
    return service.create(Example=Example)


@router.patch("/")
def modify(Example: Example) -> Example:
    return service.modify(Example=Example)


@router.put("/")
def replace(Example: Example) -> Example:
    return service.replace(Example=Example)


@router.delete("/{name}")
def delete(name: str):
    return None