import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)

from sqlalchemy.orm import Session
from app.core.config import Settings
from app.schemas.recipe_ingredient import RecipeIngredientModel

# from app.crud.book import get_book_by_id
from app.crud.recipe_ingredient import create_recipe_ingredient

logger = logging.getLogger('recipebox')
settings = Settings()


def init_rec_ing(db: Session):
    create_init_recipe_ingredient(db)


def create_init_recipe_ingredient(db: Session):
    recipe_ingredient = settings.INIT_RECIPE_INGREDIENT
    # try:
    #     db_recipe_ingredient = RecipeIngredientModel(
    #         recipe_id=recipe_ingredient['recipe_id'],
    #         ingredient_id=recipe_ingredient["ingredient_id"],
    #         quantity=recipe_ingredient['quantity']
    #     )
    #     create_recipe_ingredient(db, db_recipe_ingredient)
    # except Exception:
    logger.error("Can't create recipe_ingredient")
    db_recipe_ingredient = RecipeIngredientModel(
        recipe_id=recipe_ingredient['recipe_id'],
        ingredient_id=recipe_ingredient["ingredient_id"],
        quantity=recipe_ingredient['quantity']
        )
    create_recipe_ingredient(db, db_recipe_ingredient)
