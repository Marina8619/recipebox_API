import logging
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.schemas.ingredient import IngredientModel
from app.models.ingredient import Ingredient

ingredient_router = APIRouter()
logger = logging.getLogger('recipebox')


@ingredient_router.get("/{ingredient_id}", response_model=IngredientModel)
def get_ingredient(ingredient_id: int, db: Session = Depends(get_db)):
    ingredient = db.query(Ingredient).filter(Ingredient.id == ingredient_id).first()
    if not ingredient:
        raise HTTPException(status_code=404, detail="Ingredient wasn't found, {ingredient_id}")
    return ingredient


@ingredient_router.get("/", response_model=List[IngredientModel])
def get_ingredients(db: Session = Depends(get_db)):
    return db.query(Ingredient).all()