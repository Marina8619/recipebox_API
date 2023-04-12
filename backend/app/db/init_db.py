import logging

from pydantic import ValidationError
from sqlalchemy.orm import Session

from app.core.config import Settings
from app.schemas.ingredient import IngredientCreateModel
from app.schemas.recipe import RecipeCreateModel
from app.schemas.user import UserCreateModel

from app.crud.ingredient import create_init_ingredient
from app.crud.recipe import create_init_recipe
from app.crud.user import create_init_user


settings = Settings()
logger = logging.getLogger('recipebox')


def init_db(db: Session):
    #create_user(db)
    #create_ingredient(db)
    create_recipe(db)



def create_user(db: Session):
    user = settings.INIT_USER
    try:
        db_user = UserCreateModel(
            username=user['username'],
            email=user['email'],
            password=user['password'],
            is_active=user['is_active'],
            role_id=user['role_id']
        )
    except ValidationError as e:
        logger.error(f"An error occur while creating model {e}")
    else:
        create_init_user(db, db_user)


def create_recipe(db: Session):
    for recipe in settings.INIT_RECIPE:
        db_recipe = RecipeCreateModel(
            name=recipe['name'],
            description=recipe['description'],
            difficulty=recipe['difficulty'],
            instructions=recipe['instructions']
        )
        create_init_recipe(db, db_recipe)


def create_ingredient(db: Session):
    for ingredient in settings.INIT_INGREDIENT:
        db_ingredient = IngredientCreateModel(
            name=ingredient['name']
        )
        create_init_ingredient(db, db_ingredient)

