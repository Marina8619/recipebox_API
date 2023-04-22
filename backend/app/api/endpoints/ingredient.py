import logging
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.schemas.ingredient import IngredientModel
from app.models.ingredient import Ingredient
from app.crud.ingredient import get_ingredient_by_id, get_ingredient_list

ingredient_router = APIRouter()
logger = logging.getLogger('recipebox')


@ingredient_router.get("/{ingredient_id}", response_model=IngredientModel)
def get_ingredient(ingredient_id: int, db: Session = Depends(get_db)):
    ingredient = get_ingredient_by_id(db, ingredient_id)
    if not ingredient:
        raise HTTPException(status_code=404, detail="Ingredient wasn't found, {ingredient_id}")
    logger.info(f"Found ingredient with id {ingredient_id}")
    return ingredient


@ingredient_router.get('/ingredients/', response_model=List[IngredientModel])
def get_ingredients(db: Session = Depends(get_db)):
    logger.info(f"Recipes viewed!")
    return get_ingredient_list(db)