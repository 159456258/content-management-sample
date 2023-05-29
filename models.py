from pydantic import BaseModel


class ContentM(BaseModel):
    Title: str
    Year: int
    Type: str
