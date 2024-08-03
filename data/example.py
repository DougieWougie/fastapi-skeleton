import os
from errors import Missing

os.environ["EXAMPLE_DB"] = ":memory:"

from data.init_sqlite import curs
from model.example import Example

curs.execute(
    """create table if not exists example(
            name text primary key,
            country text,
            description text)"""
)


def row_to_model(row: tuple) -> Example:
    return Example(name=row[0], country=row[1], description=row[2])


def model_to_dict(example: Example) -> dict:
    return example.model_dump() if example else None


def get_one(name: str) -> Example:
    qry = "select * from example where name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row=row)
    else:
        raise Missing(msg=f"Example {name} not found")


def get_all() -> list[Example]:
    qry = "select * from example"
    curs.execute(qry)
    return [row_to_model(row) for row in curs.fetchall()]


def create(example: Example) -> Example:
    qry = """insert into example (name, country, description)
    values (:name, :country, :description)"""
    params = model_to_dict(example)
    _ = curs.execute(qry, params)
    return get_one(example.name)


def modify(name: str, example: Example) -> Example:
    qry = """update example
    set country=:country,
    name=:name,
    description=:description
    where name=:name_orig"""
    params = model_to_dict(example)
    params["name_orig"] = example.name
    _ = curs.execute(qry, params)
    explorer2 = get_one(example.name)
    return explorer2


def delete(example: Example) -> bool:
    qry = "delete from example where name = :name"
    params = {"name": example.name}
    res = curs.execute(qry, params)
    return bool(res)
