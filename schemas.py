from datetime import date
from pydantic import BaseModel


class CreateAuthorRequest(BaseModel):
    name: str
    bio: str


class GetAuthorResponse(CreateAuthorRequest):
    id: int
    name: str
    bio: str

    class Config:
        orm_mode = True


class GetAuthorsBooks(BaseModel):
    class Meta:
        orm_mode = True


class CreateBookRequest(BaseModel):
    title: str
    summary: str
    publication_date: date
    author_id: int

    class Config:
        from_attributes = True


class GetBookResponse(CreateBookRequest):
    id: int
