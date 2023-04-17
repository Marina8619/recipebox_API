from typing import Optional
from pydantic import BaseModel, Field


class IngredientBaseModel(BaseModel):
    name: str
    units: Optional[str]


class IngredientCreateModel(IngredientBaseModel):
    pass


class IngredientUpdateModel(IngredientBaseModel):
    pass


class IngredientOutModel(IngredientBaseModel):
    id: int
    name: str = Field(..., alias='ingredient_name')
    units: str = Field(..., alias='ingredient_units')

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class IngredientModel(IngredientBaseModel):
    id: int

    class Config:
        orm_mode = True
