import os
from fastapi import APIRouter, HTTPException
from model.example import Example

if os.getenv("EXAMPLE_UNIT_TEST"):
    from fake import example as service
else:
    from service import example as service
from errors import Duplicate, Missing

router = APIRouter(prefix="/example")


@router.get("")
@router.get("/")
def get_all() -> list[Example]:
    return service.get_all()


@router.get("/{name}")
def get_one(name) -> Example:
    try:
        return service.get_one(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


@router.post("", status_code=201)
@router.post("/", status_code=201)
def create(example: Example) -> Example:
    try:
        return service.create(example)
    except Duplicate as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


@router.patch("/")
def modify(name: str, example: Example) -> Example:
    try:
        return service.modify(name, example)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


@router.delete("/{name}", status_code=204)
def delete(name: str):
    try:
        return service.delete(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)
