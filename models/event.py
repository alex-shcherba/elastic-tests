from pydantic import BaseModel


class Event(BaseModel):
    dataset: str
