from pydantic import BaseModel


class Example(BaseModel):
    """Example model"""
    name: str
    country: str
    description: str