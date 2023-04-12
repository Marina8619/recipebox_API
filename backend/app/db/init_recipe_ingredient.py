import logging

from app.crud.recipe_ingredient import create_recipe_ingredient
from app.schemas.recipe_ingredient import RecipeIngredientCreateModel

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
from sqlalchemy.orm import Session
from app.core.config import Settings


logger = logging.getLogger('recipebox')
settings = Settings()


def init_rec_ing(db: Session):
    create_init_recipe_ingredient(db)


def create_init_recipe_ingredient(db: Session):
    recipe_ingredient = settings.INIT_RECIPE_INGREDIENT
    if isinstance(recipe_ingredient, list):
        for r in recipe_ingredient:
            db_recipe_ingredient = RecipeIngredientCreateModel(
                recipe_id=r['recipe_id'],
                ingredient_id=r["ingredient_id"],
                quantity=r['quantity']
            )
            create_recipe_ingredient(db, db_recipe_ingredient)
    else:
        db_recipe_ingredient = RecipeIngredientCreateModel(
            recipe_id=recipe_ingredient['recipe_id'],
            ingredient_id=recipe_ingredient["ingredient_id"],
            quantity=recipe_ingredient['quantity']
        )
        create_recipe_ingredient(db, db_recipe_ingredient)
