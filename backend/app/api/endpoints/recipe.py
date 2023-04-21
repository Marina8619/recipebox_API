import logging
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import Float
from sqlalchemy.orm import Session
from app.db.session import get_db

from app.schemas.recipe import RecipeModel
from app.models.recipe import Recipe

from app.crud.recipe import get_recipe_by_id, get_recipe_list

from app.crud.recipe import create_add_recipe
# from app.crud.recipe_ingredient import create_add_recipe_ingredient
#
# from app.schemas.recipe import RecipeCreateModel
#
# from app.schemas.recipe import RecIngModel
# from app.schemas.recipe_ingredient import RecipeIngredientModel
#
# from app.models.recipe import RecIng

recipe_router = APIRouter()
logger = logging.getLogger('recipebox')


@recipe_router.get("/receipts/{receipt_id}", response_model=RecipeModel)
def get_receipt(receipt_id: int, db: Session = Depends(get_db)):
    if receipt := get_recipe_by_id(db, receipt_id):
        logger.info(f"Found receipt of {receipt.name}")
        return receipt
    else:
        return HTTPException(status_code=404, detail="Recipe wasn't found")


@recipe_router.get('/receipts/', response_model=List[RecipeModel])
def get_receipts(db: Session = Depends(get_db)):
    return get_recipe_list(db)


@recipe_router.get("/recipes/{recipe_name}", response_model=RecipeModel)
async def get_recipe_by_name(recipe_name: str, db: Session = Depends(get_db)):
    recipe = db.query(Recipe).filter(Recipe.name == recipe_name).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe


@recipe_router.post("/recipes/", response_model=RecipeModel)
def create_recipe(recipe: RecipeModel, db: Session = Depends(get_db)):
    return create_add_recipe(db, Recipe(
        name=recipe.name,
        description=recipe.description,
        difficulty=recipe.difficulty,
        instructions=recipe.instructions,
        user_id=recipe.user_id
    ))


# при запросе требует имя name
# @recipe_router.post("/recipes/", response_model=RecIngModel)
# def create_recipe(recipe: RecIngModel, db: Session = Depends(get_db)):
#     new_recipe = create_add_recipe(db, Recipe(
#         name=recipe.name,
#         description=recipe.description,
#         difficulty=recipe.difficulty,
#         instructions=recipe.instructions,
#         user_id=recipe.user_id
#     ))
#     new_recipe_ingredient = create_add_recipe_ingredient(db, RecipeIngredientModel(
#         recipe_id=new_recipe.recipe_id,
#         ingredient_id=new_recipe.ingredient_id,
#         quantity=new_recipe.quantity
#     ))
#     return RecIng(new_recipe, new_recipe_ingredient)



