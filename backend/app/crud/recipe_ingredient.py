import logging
from sqlalchemy.orm import Session

from typing import Dict, Any
from app.models.recipe_ingredient import RecipeIngredient

logger = logging.getLogger('recipebox')


def create_recipe_ingredient(db: Session, recipe_ingredient: RecipeIngredient) -> RecipeIngredient:
    db_recipe_ingredient = RecipeIngredient(
        recipe_id=recipe_ingredient.recipe_id,
        ingredient_id=recipe_ingredient.ingredient_id,
        quantity=recipe_ingredient.quantity
    )
    logger.info(f"Recipe ingredient {recipe_ingredient} created")
    return db_recipe_ingredient


