import logging
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db

from app.schemas.recipe import RecipeModel
from app.models.recipe import Recipe

from app.crud.recipe import get_recipe_by_id, get_recipe_list


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


@recipe_router.get("/receipts/{receipt_name}", response_model=RecipeModel)
async def get_recipe_by_name(receipt_name: str, db: Session = Depends(get_db)):
    recipe = db.query(Recipe).filter(Recipe.name == receipt_name).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe
