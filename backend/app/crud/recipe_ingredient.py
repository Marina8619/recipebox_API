import logging
from sqlalchemy.orm import Session

from typing import List
from app.models.recipe_ingredient import RecipeIngredient
# from app.schemas.recipe_ingredient import RecipeIngredientModel


logger = logging.getLogger('recipebox')


def create_recipe_ingredient(db: Session, recipe_ingredient: RecipeIngredient) -> List[RecipeIngredient]:
    db_recipe_ingredient = RecipeIngredient(
        recipe_id=recipe_ingredient.recipe_id,
        ingredient_id=recipe_ingredient.ingredient_id,
        quantity=recipe_ingredient.quantity
    )

    db.add(db_recipe_ingredient)
    db.commit()
    db.refresh(db_recipe_ingredient)

    logger.info(f"Recipe ingredient {recipe_ingredient} created")
    return db_recipe_ingredient

