import logging
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.recipe_ingredient import RecipeIngredient

from app.models.ingredient import Ingredient
from app.models.recipe import Recipe
from app.schemas.recipe_ingredient import RecipeWithIngredients

rec_ing_router = APIRouter()
logger = logging.getLogger('recipebox')


@rec_ing_router.get("/recipes with ingredients/{recipe_id}")
async def get_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    ingredients = (
        db.query(Ingredient, RecipeIngredient.quantity)
        .join(RecipeIngredient)
        .filter(RecipeIngredient.recipe_id == recipe_id)
        .all()
    )
    recipe_ingredients = [
        {"name": ingredient.name, "quantity": quantity} for ingredient, quantity in ingredients
    ]
    return {"id": recipe.id, "name": recipe.name, "ingredients": recipe_ingredients}





# @rec_ing_router.get("/recipes-with-ingredients")
# async def get_recipes_with_ingredients(db: Session = Depends(get_db)):
#     recipes = db.query(RecipeIngredient.recipe_id, Recipe.name, Ingredient.name, RecipeIngredient.quantity).\
#         join(Recipe).\
#         join(Ingredient).\
#         all()
#     recipe_ingredients = []
#     for recipe in recipes:
#         recipe_id, recipe_name, ingredient_name, quantity = recipe
#         recipe_found = next((ri for ri in recipe_ingredients if ri["id"] == recipe_id), None)
#         if recipe_found is None:
#             recipe_found = {"id": recipe_id, "name": recipe_name, "ingredients": []}
#             recipe_ingredients.append(recipe_found)
#         recipe_found["ingredients"].append({"name": ingredient_name, "quantity": quantity})
#     return recipe_ingredients





# Получение всех рецептов с ингредиентами
# @rec_ing_router.get("/recipes_with_ingredients")
# async def get_recipes_with_ingredients(db: Session = Depends(get_db)):
#     recipes = db.query(Recipe).all()
#     result = []
#     for recipe in recipes:
#         ingredients = (
#             db.query(Ingredient, RecipeIngredient.quantity)
#             .join(RecipeIngredient)
#             .filter(RecipeIngredient.recipe_id == recipe.id)
#             .all()
#         )
#         recipe_ingredients = [
#             {"name": ingredient.name, "quantity": quantity} for ingredient, quantity in ingredients
#         ]
#         result.append({"id": recipe.id, "name": recipe.name, "ingredients": recipe_ingredients})
#     return result


# @rec_ing_router.get("/{recipe_id_with_ingredient}", response_model=False)
# def get_recipe_by_id(recipe_id: int, db: Session = Depends(get_db)):
#     """
#     Получить рецепт и список ингредиентов по id рецепта
#     """
#     recipe_ingredients = (
#         db.query(RecipeIngredient)
#         .filter(RecipeIngredient.recipe_id == recipe_id)
#         .all()
#     )
#
#     if not recipe_ingredients:
#         raise HTTPException(status_code=404, detail="Recipe wasn't found")
#
#     recipe_ingredients_schema = []
#
#     for ri in recipe_ingredients:
#         ingredient_schema = {
#             "id": ri.ingredient.id,
#             "name": ri.ingredient.name,
#             "quantity": ri.quantity,
#             "units": ri.ingredient.units,
#         }
#         recipe_ingredients_schema.append(ingredient_schema)
#
#     recipe_name = recipe_ingredients[0].recipe.name
#
#     return {"recipe_name": recipe_name, "ingredients": recipe_ingredients_schema}







# [
#   {
#     "name": "omelet",
#     "description": "a great breakfast option",
#     "difficulty": 2,
#     "instructions": "mix all the ingredients and put in the oven for 20 minutes",
#     "user_id": "1",
#     "id": 1
#   },
#   {
#     "name": "rice milk soup",
#     "description": "instant soup",
#     "difficulty": 1,
#     "instructions": "cook rice for 20 minutes, add milk and bring to a boil",
#     "user_id": "1",
#     "id": 2
#   }
# ]
#
# [
#   {
#     "id": 1,
#     "name": "egg",
#     "units": "unit"
#   },
#   {
#     "id": 2,
#     "name": "milk",
#     "units": "ml"
#   },
#   {
#     "id": 3,
#     "name": "salt",
#     "units": "mg"
#   },
#   {
#     "id": 4,
#     "name": "water",
#     "units": "ml"
#   },
#   {
#     "id": 5,
#     "name": "rise",
#     "units": "g"
#   }
# ]


