import logging
from sqlalchemy.orm import Session


from app.models.recipe_ingredient import RecipeIngredient

logger = logging.getLogger('recipebox')


def create_recipe_ingredient(db: Session, recipe_ingredient:  RecipeIngredient) -> RecipeIngredient:
    recipe_ingredient = RecipeIngredient(
        recipe_id=recipe_ingredient.recipe_id,
        ingredient_id=recipe_ingredient.ingredient_id,
        quantity=recipe_ingredient.quantity
    )
    db.add(recipe_ingredient)
    db.commit()
    db.refresh(recipe_ingredient)
    return recipe_ingredient

