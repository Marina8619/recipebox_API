from pydantic import BaseModel


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


class Recipe(RecipeBaseModel):
    id: int

    class Config:
        orm_mode = True


class RecipeModel(RecipeBaseModel):
    id: int

    class Config:
        orm_mode = True


# from typing import List
# from pydantic import BaseModel
#
#
# class RecipeBaseSchema(BaseModel):
#     name: str
#     description: str
#     difficulty: int
#     instructions: str
#     user_id: int
#
#
# class RecipeSchema(RecipeBaseModel):
#     id: int
#
#     class Config:
#         orm_mode = True