from pydantic import BaseModel


class ContentM(BaseModel):
    title: str
    year: int
    type: str
