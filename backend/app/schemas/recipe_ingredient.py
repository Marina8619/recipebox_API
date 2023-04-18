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


# class RecipeIngredientModel(BaseModel):
#     recipe_id: int
#     ingredient_id: int
#     quantity: float
#
# class RecipeIngredientSchema(BaseModel):
#     id: int
#     recipe_id: int
#     ingredient_id: int
#     quantity: float
#     ingredient: Optional[IngredientSchema]
#
#     class Config:
#         orm_mode = True


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


# class IngredientQuantity(BaseModel):
#     name: str
#     quantity: float
#     units: str
