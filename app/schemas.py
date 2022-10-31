from pydantic import BaseModel


class CountryBase(BaseModel):
    title: str
    description: str | None = None


class CountryCreate(CountryBase):
    pass


class Country(CountryBase):
    id: int

    class Config:
        orm_mode = True
