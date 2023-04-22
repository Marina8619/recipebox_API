import logging
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import Float
from sqlalchemy.orm import Session
from app.db.session import get_db

from app.schemas.recipe import RecipeModel
from app.models.recipe import Recipe

from app.crud.recipe import get_recipe_by_id, get_recipe_list, get_recipe_by_name

from app.crud.recipe import create_add_recipe



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
    logger.info(f"Recipes viewed")
    return get_recipe_list(db)


@recipe_router.get("/recipes/{recipe_name}", response_model=RecipeModel)
async def get_recipe_name(recipe_name: str, db: Session = Depends(get_db)):
    recipe = get_recipe_by_name(db, recipe_name)
    logger.info(f"Found receipt of {recipe_name}")
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe


@recipe_router.post("/recipes/", response_model=RecipeModel)
def create_recipe(recipe: RecipeModel, db: Session = Depends(get_db)):
    logger.info(f"Create new recipe!")
    return create_add_recipe(db, Recipe(
        name=recipe.name,
        description=recipe.description,
        difficulty=recipe.difficulty,
        instructions=recipe.instructions,
        user_id=recipe.user_id
    ))


@recipe_router.delete("/recipes/{recipe_id}")
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = get_recipe_by_id(db, recipe_id)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    db.delete(recipe)
    db.commit()
    logger.info(f"Delete recipe with id {recipe_id}")
    return {"message": "Recipe successfully deleted"}


@recipe_router.get('/receipts_difficulty/', response_model=List[RecipeModel])
def get_receipts(sort_by_difficulty: bool = False, db: Session = Depends(get_db)):
    recipe_list = get_recipe_list(db)
    if sort_by_difficulty:
        recipe_list.sort(key=lambda x: x.difficulty)
    logger.info(f"Sort recipes by difficulty!")
    return recipe_list


@recipe_router.put('/recipes/{recipe_id}/instructions/')
def update_recipe_instructions(recipe_id: int, instructions: str, db: Session = Depends(get_db)):
    recipe = get_recipe_by_id(db, recipe_id)
    if not recipe:
        raise HTTPException(status_code=404, detail='Recipe not found')
    recipe.instructions = instructions
    db.commit()
    db.refresh(recipe)
    logger.info(f"Update recipe of with id {recipe_id}")
    return recipe





