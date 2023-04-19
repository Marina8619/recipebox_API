from typing import List, Optional

from pydantic import BaseModel


class RecipeIngredientBaseModel(BaseModel):
    recipe_id: int
    ingredient_id: int
    quantity: float


class RecipeIngredientCreateModel(RecipeIngredientBaseModel):
    pass


class RecipeIngredientUpdateModel(RecipeIngredientBaseModel):
    pass


class RecipeIngredientModel(RecipeIngredientBaseModel):
    id: int

    class Config:
        orm_mode = True


class IngredientSchema(BaseModel):
    id: int
    name: str
    quantity: float
    units: str


class RecipeIngredientsResponseSchema(BaseModel):
    recipe_name: str
    ingredients: List[IngredientSchema]


class RecipeWithIngredients(BaseModel):
    id: int
    name: str
    ingredients: List[IngredientSchema]
    quantity: int
    description: str
    difficulty: int
    instructions: str

    class Config:
        orm_mode = True
