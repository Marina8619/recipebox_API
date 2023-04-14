import logging
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db

from app.schemas.recipe import RecipeModel
from app.models.recipe import Recipe
from app.crud.recipe import get_recipe_list


recipe_router = APIRouter()
logger = logging.getLogger('recipebox')


# @recipe_router.get('/recipe/{recipe_id}', response_model=RecipeModel)
# def get_recipe(recipe_id: int, db: Session = Depends(get_db)) -> Recipe:
#     if db_recipe := get_recipe_by_id(db, recipe_id):
#         logger.info(msg=f"Get recipe {db_recipe.first_name}, {db_recipe.last_name}")
#         return db_recipe
#     else:
#         logger.error(f'Recipe does\'t with id={recipe_id} exist')
#         raise HTTPException(status_code=404, detail=f'Recipe does\'t with id={recipe_id} exist')


@recipe_router.get("/{recipe_id}", response_model=RecipeModel)
def get_recipe_by_id(recipe_id: int, db: Session = Depends(get_db)):
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe wasn't found")
    return recipe


@recipe_router.get('/', response_model=List[RecipeModel])
async def get_recipe_list(db: Session = Depends(get_db)):
    return db.query(Recipe).all()