import logging

from app.crud.recipe_ingredient import create_recipe_ingredient
from app.crud.ingredient import create_init_ingredient
from app.crud.recipe import create_init_recipe

from app.schemas.recipe_ingredient import RecipeIngredientCreateModel
from app.schemas.ingredient import IngredientCreateModel
from app.schemas.recipe import RecipeCreateModel


# Set up logging configuration
logging.basicConfig(level=logging.INFO)
from sqlalchemy.orm import Session
from app.core.config import Settings

# # from app.crud.book import get_book_by_id
# from app.crud.recipe_ingredient import create_recipe_ingredient

logger = logging.getLogger('recipebox')
settings = Settings()


def init_rec_ing(db: Session):
    #create_ingredient(db)
    #create_recipe(db)
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


def create_recipe(db: Session):
    for recipe in settings.INIT_RECIPE:

        db_recipe = RecipeCreateModel(
            name=recipe['name'],
            description=recipe['description'],
            difficulty=recipe['difficulty'],
            instructions=recipe['instructions'],
            user_id=recipe['user_id']
        )
        create_init_recipe(db, db_recipe)


def create_ingredient(db: Session):
    for ingredient in settings.INIT_INGREDIENT:
        db_ingredient = IngredientCreateModel(
            name=ingredient['name'],
            units=ingredient['units']
        )
        create_init_ingredient(db, db_ingredient)