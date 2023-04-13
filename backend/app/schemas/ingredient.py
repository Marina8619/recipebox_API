from typing import Optional

from pydantic import BaseModel


class IngredientBaseModel(BaseModel):
    name: str
    units: Optional[str]


class IngredientCreateModel(IngredientBaseModel):
    pass


class IngredientUpdateModel(IngredientBaseModel):
    pass


class IngredientModel(IngredientBaseModel):
    id: int

    class Config:
        orm_mode = True