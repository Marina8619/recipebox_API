from typing import Optional

from pydantic import BaseModel, Field
from .recipe import Recipe


class IngredientBaseModel(BaseModel):
    name: str
    units: Optional[str]


class IngredientCreateModel(IngredientBaseModel):
    pass


class IngredientUpdateModel(IngredientBaseModel):
    pass


class IngredientOutModel(IngredientBaseModel):
    id: int
    name: str = Field(alias='ingredient_name')
    units: Optional[str] = Field(alias='units')

    recipes: Recipe = Field(alias='recipe_ingredient')
    # id: int
    # title: str = Field(alias='book_title')
    # description: str = Field(alias='book_description')
    # price: float = Field(..., exclude=True, alias='book_price')
    # author_id: int = Field(..., exclude=True, alias='book_author_id')
    # amount: int = Field(..., exclude=True)
    # author: AuthorModel = Field(alias='book_author')

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class IngredientModel(IngredientBaseModel):
    id: int
    recipe_id: int = Field(..., exclude=True)
    recipe: Recipe

    class Config:
        orm_mode = True


#created for the endpoint
class IngredientSchema(BaseModel):
    id: int
    name: str
    units: str

    class Config:
        orm_mode = True

