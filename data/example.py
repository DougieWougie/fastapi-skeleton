from .init_sqlite import curs, IntegrityError
from model.example import Example
from errors import Missing, Duplicate

curs.execute(
    """create table if not exists example(
                name primary key,
                country text,
                description text)"""
)


def row_to_model(row: tuple) -> Example:
    name, country, description = row
    return Example(name=name, country=country, description=description)


def model_to_dict(example: Example) -> dict:
    return example.model_dump()


def get_one(name: str) -> Example:
    qry = "select * from example where name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(msg=f"Example {name} not found")


def get_all() -> list[Example]:
    qry = "select * from example"
    curs.execute(qry)
    return [row_to_model(row) for row in curs.fetchall()]


def create(example: Example) -> Example:
    if not example:
        return None
    qry = """insert into example
             (name, country, description) values
             (:name, :country, :description)"""
    params = model_to_dict(example)
    try:
        curs.execute(qry, params)
    except IntegrityError:
        raise Duplicate(msg=f"Example {example.name} already exists")
    return get_one(example.name)


def modify(name: str, example: Example) -> Example:
    if not (name and example):
        return None
    qry = """update example
             set name=:name, country=:country,
                 description=:description
             where name=:orig_name"""
    params = model_to_dict(example)
    params["orig_name"] = name
    curs.execute(qry, params)
    if curs.rowcount == 1:
        return get_one(example.name)
    else:
        raise Missing(msg=f"Example {name} not found")


def delete(name: str):
    if not name:
        return False
    qry = "delete from example where name = :name"
    params = {"name": name}
    curs.execute(qry, params)
    if curs.rowcount != 1:
        raise Missing(msg=f"Example {name} not found")
