from typing import List

from pydantic import BaseModel
from .ingredient import IngredientOutModel
from .recipe_ingredient import RecipeIngredientModel


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


class RecIngModel(BaseModel):
    recipe: RecipeModel
    rec_ing: List[RecipeIngredientModel]
