from typing import List

from pydantic import BaseModel
from .ingredient import IngredientOutModel


class RecipeBaseModel(BaseModel):
    name: str
    description: str
    difficulty: int
    instructions: str
    user_id: str


class RecipeCreateModel(RecipeBaseModel):
    pass


class RecipeUpdateModel(RecipeBaseModel):
    pass


class RecipeModel(RecipeBaseModel):
    id: int
    ingredients: List[IngredientOutModel]

    class Config:
        orm_mode = True