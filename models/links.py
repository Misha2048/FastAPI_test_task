from pydantic import BaseModel


class HTMLModel(BaseModel):
    link: str
    html: str
