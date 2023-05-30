from pydantic import BaseModel, Extra
from typing import List, Optional


class ContentM(BaseModel):
    Title: Optional[str] = None
    Year: Optional[int] = None
    Type: Optional[str] = None

    class Config:
        extra = Extra.forbid


class ContentC(BaseModel):
    Title: str
    Year: int
    Type: str


