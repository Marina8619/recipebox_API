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
