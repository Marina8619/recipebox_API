from pydantic import BaseModel


class RecipeBaseModel(BaseModel):
    name: str
    description: str
    difficulty: int
    instructions: str


class RecipeCreateModel(RecipeBaseModel):
    pass


class RecipeUpdateModel(RecipeBaseModel):
    pass


class Recipe(RecipeBaseModel):
    id: int

    class Config:
        orm_mode = True